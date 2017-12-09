$(document).ready(function() {
  $('.checkbox').click(function() {
    $(this).parent().submit();
  });
});
