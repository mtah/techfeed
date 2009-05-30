$(document).ready(function() {
  /* event handlers for focus/blur of text fields, provide default text */
  $('input[type="text"]').focus(function() {
    if (this.value == this.defaultValue) this.value = '';
  });
  $('input[type="text"]').blur(function() {
    if (this.value == '') this.value = (this.defaultValue ? this.defaultValue : '');
  });
});
