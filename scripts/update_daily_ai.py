#!/usr/bin/env python3
"""Update the Daily AI page from Develata's AI_ML daily feed.

The generated page keeps the feed's item metadata and original links, then
adds short local "Why read" notes instead of copying the source summaries.
"""

from __future__ import annotations

import argparse
import html as html_lib
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from zoneinfo import ZoneInfo


DEFAULT_BASE_URL = "https://develata.me/news/AI_ML"
DEFAULT_OUTPUT = Path("_pages/daily-papers.md")
DEFAULT_MAX_ITEMS = 12
DEFAULT_FALLBACK_DAYS = 7
TIMEZONE = ZoneInfo("Asia/Shanghai")


@dataclass(frozen=True)
class FeedItem:
    title: str
    score: str
    tags: tuple[str, ...]
    source: str
    href: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate _pages/daily-papers.md from the latest AI_ML feed.")
    parser.add_argument("--date", default=os.getenv("DAILY_AI_DATE", ""), help="Feed date as YYYYMMDD or YYYY-MM-DD.")
    parser.add_argument("--base-url", default=os.getenv("DAILY_AI_BASE_URL", DEFAULT_BASE_URL))
    parser.add_argument("--output", default=os.getenv("DAILY_AI_OUTPUT", str(DEFAULT_OUTPUT)))
    parser.add_argument("--max-items", type=int, default=int(os.getenv("DAILY_AI_MAX_ITEMS", DEFAULT_MAX_ITEMS)))
    parser.add_argument("--fallback-days", type=int, default=int(os.getenv("DAILY_AI_FALLBACK_DAYS", DEFAULT_FALLBACK_DAYS)))
    return parser.parse_args()


def parse_feed_date(value: str) -> date | None:
    value = value.strip()
    if not value:
        return None
    for fmt in ("%Y%m%d", "%Y-%m-%d"):
        try:
            return datetime.strptime(value, fmt).date()
        except ValueError:
            pass
    raise SystemExit(f"Invalid DAILY_AI_DATE: {value!r}. Use YYYYMMDD or YYYY-MM-DD.")


def candidate_dates(requested_date: date | None, fallback_days: int) -> Iterable[date]:
    if requested_date:
        yield requested_date
        return
    today = datetime.now(TIMEZONE).date()
    for offset in range(max(1, fallback_days + 1)):
        yield today - timedelta(days=offset)


def feed_url(base_url: str, day: date) -> str:
    stamp = day.strftime("%Y%m%d")
    return f"{base_url.rstrip('/')}/{day:%Y}/{stamp}"


def fetch_url(url: str) -> str:
    request = Request(
        url,
        headers={
            "User-Agent": "lern-to-write-daily-ai-updater/1.0 (+https://lern-to-write.github.io/)",
            "Accept": "text/html,application/xhtml+xml",
        },
    )
    with urlopen(request, timeout=30) as response:
        charset = response.headers.get_content_charset() or "utf-8"
        return response.read().decode(charset, "replace")


def text_from_html(fragment: str) -> str:
    fragment = re.sub(r"<!--.*?-->", "", fragment, flags=re.S)
    fragment = re.sub(r"<br\s*/?>", " ", fragment, flags=re.I)
    fragment = re.sub(r"<[^>]+>", " ", fragment)
    text = html_lib.unescape(fragment)
    text = text.replace("\u200b", "")
    return re.sub(r"\s+", " ", text).strip()


def extract_main(html_text: str) -> str:
    start = html_text.find('<main class="main"')
    if start == -1:
        raise ValueError("Could not find VitePress main content.")
    end = html_text.find("</main>", start)
    if end == -1:
        raise ValueError("Could not find end of VitePress main content.")
    return html_text[start:end]


def extract_page_date(main_html: str, fallback: date) -> str:
    match = re.search(r"<h1\b[^>]*>(.*?)</h1>", main_html, flags=re.S)
    if not match:
        return fallback.strftime("%Y-%m-%d")
    text = text_from_html(match.group(1))
    found = re.search(r"\d{4}-\d{2}-\d{2}", text)
    return found.group(0) if found else fallback.strftime("%Y-%m-%d")


def extract_items(html_text: str) -> list[FeedItem]:
    main_html = extract_main(html_text)
    items: list[FeedItem] = []
    item_pattern = re.compile(r"<h2\b[^>]*>(.*?)</h2>(.*?)(?=<hr>|<h2\b|</div>\s*</main>)", re.S)

    for match in item_pattern.finditer(main_html):
        title_html, body_html = match.groups()
        score_match = re.search(r'<span\b[^>]*class="[^"]*VPBadge[^"]*"[^>]*>.*?(\d{1,3}).*?</span>', title_html, re.S)
        score = score_match.group(1) if score_match else "0"

        title_html = re.sub(r'<span\b[^>]*class="[^"]*VPBadge[^"]*"[^>]*>.*?</span>', "", title_html, flags=re.S)
        title_html = re.sub(r'<a\b[^>]*class="header-anchor"[^>]*>.*?</a>', "", title_html, flags=re.S)
        title = text_from_html(title_html)
        if not title:
            continue

        tags_match = re.search(r"<strong>\s*Tags:\s*</strong>(.*?)</p>", body_html, flags=re.S)
        tags = tuple(text_from_html(tag) for tag in re.findall(r"<code>(.*?)</code>", tags_match.group(1), flags=re.S)) if tags_match else ()

        source_match = re.search(
            r'<strong>\s*Source:\s*</strong>\s*<code>(.*?)</code>\s*\|\s*<a\b[^>]*href="([^"]+)"',
            body_html,
            flags=re.S,
        )
        if source_match:
            source = text_from_html(source_match.group(1))
            href = html_lib.unescape(source_match.group(2)).strip()
        else:
            source = "Develata"
            href = ""

        if href and not re.match(r"^https?://", href):
            href = ""

        items.append(FeedItem(title=title, score=score, tags=tags, source=source, href=href))

    return items


def why_read(item: FeedItem) -> str:
    text = " ".join((item.title, *item.tags))
    rules = [
        ("智能体", "适合关注 agent 产品化、工具调用、路由和执行闭环的人，先看它怎样影响成本、评测和真实工作流。"),
        ("语音", "语音交互正在从 demo 走向可配置产品，重点看实时性、稳定性、评测指标和接入成本。"),
        ("多模态", "多模态能力仍是应用落地的关键变量，重点看视觉 grounding、幻觉控制和偏好对齐。"),
        ("开源", "开源生态信号值得跟进，重点看权重许可、复现实验、推理成本和社区可用性。"),
        ("开放权重", "开放权重路线会影响可复现研究和本地部署，先看模型结构、许可证和吞吐量表现。"),
        ("模型发布", "新模型发布适合快速扫能力边界，重点看上下文、推理效率、训练基础设施和生态影响。"),
        ("推理优化", "推理效率和 inference-time scaling 继续升温，重点看质量收益、延迟成本和稳定性。"),
        ("训练方法", "训练方法类工作适合沉淀为实验思路，重点看数据选择、目标函数和是否容易复现。"),
        ("理论", "偏理论内容适合补齐判断框架，重点看它解释了哪些经验现象，以及能否指导新实验。"),
        ("AI安全", "安全与对齐类内容适合放进长期跟踪列表，重点看失败模式、评测设置和缓解手段。"),
        ("成本优化", "工程实践价值在于帮你少走弯路，重点看路由、缓存、降级和不同模型之间的性价比。"),
    ]
    for keyword, note in rules:
        if keyword in text:
            return note
    return "适合快速判断今天 AI/ML 方向的新信号，先看问题设定、方法差异和是否能转化成自己的实验或产品想法。"


def escape(text: str) -> str:
    return html_lib.escape(text, quote=True)


def render_code_tags(tags: tuple[str, ...]) -> str:
    return " ".join(f"<code>{escape(tag)}</code>" for tag in tags) or "<code>AI/ML</code>"


def render_page(page_date: str, source_url: str, items: list[FeedItem]) -> str:
    tag_counter = Counter(tag for item in items for tag in item.tags)
    top_tags = "、".join(tag for tag, _ in tag_counter.most_common(6)) or "大模型、智能体、推理优化"

    parts = [
        "---",
        "permalink: /daily-papers/",
        'title: "Daily AI"',
        "author_profile: true",
        "---",
        "",
        '<div class="lab-page daily-papers-page daily-digest-page">',
        '  <article class="daily-digest p-card" aria-label="Daily AI/ML digest">',
        '    <header class="daily-digest-header">',
        '      <p class="lab-kicker">AI_ML</p>',
        f"      <h1>{escape(page_date)}</h1>",
        "      <blockquote>",
        f"        今日 AI/ML 热点快读：{escape(top_tags)}。本页每天自动从公开 daily feed 提取标题、分数、标签和原文链接，再生成本站自己的 brief。",
        "      </blockquote>",
        '      <p class="digest-source-note">',
        f'        Seed feed: <a href="{escape(source_url)}">Develata AI_ML {escape(page_date)}</a>. Each item links back to its original source. This page updates automatically.',
        "      </p>",
        "    </header>",
        "",
    ]

    for index, item in enumerate(items):
        if index:
            parts.extend(["    <hr>", ""])
        href = escape(item.href or source_url)
        parts.extend(
            [
                '    <section class="digest-item">',
                f"      <h2>{escape(item.title)} <span>{escape(item.score)}</span></h2>",
                '      <ul class="digest-meta">',
                f"        <li>Tags: {render_code_tags(item.tags)}</li>",
                f'        <li>Source: <code>{escape(item.source)}</code> | <a href="{href}">阅读原文</a></li>',
                "      </ul>",
                f"      <blockquote><strong>[Why read]</strong> {escape(why_read(item))}</blockquote>",
                "    </section>",
                "",
            ]
        )

    parts.extend(["  </article>", "</div>", ""])
    return "\n".join(parts)


def main() -> int:
    args = parse_args()
    requested_date = parse_feed_date(args.date)

    failures: list[str] = []
    for day in candidate_dates(requested_date, args.fallback_days):
        url = feed_url(args.base_url, day)
        try:
            html_text = fetch_url(url)
            items = extract_items(html_text)
        except (HTTPError, URLError, TimeoutError, ValueError) as exc:
            failures.append(f"{url}: {exc}")
            continue

        if not items:
            failures.append(f"{url}: no feed items found")
            continue

        main_html = extract_main(html_text)
        page_date = extract_page_date(main_html, day)
        selected = items[: max(1, args.max_items)]
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(render_page(page_date, url, selected), encoding="utf-8")
        print(f"Updated {output} with {len(selected)} items from {url}")
        return 0

    print("Could not update Daily AI feed.", file=sys.stderr)
    for failure in failures:
        print(f"- {failure}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
