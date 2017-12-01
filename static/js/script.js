$(document).ready(function() {
    $('.dropdown-hover').mouseover(function() {
      $('.dropdown-menu').show();
    });  
    $('.dropdown-hover').mouseleave(function() {
      $('.dropdown-menu').hide();
    });
});

function formValid() {
    alert("Thank you for contacting us. We will be in touch shortly.");
}