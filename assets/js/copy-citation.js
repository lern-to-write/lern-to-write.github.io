// Copy citation functionality
function copyToClipboard(text, btnId) {
  navigator.clipboard.writeText(text).then(function() {
    var btn = document.getElementById(btnId);
    var originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fa fa-check" aria-hidden="true"></i> Copied!';
    btn.style.color = '#28a745';
    setTimeout(function() {
      btn.innerHTML = originalText;
      btn.style.color = '';
    }, 2000);
  }, function(err) {
    console.error('Could not copy text: ', err);
  });
}
