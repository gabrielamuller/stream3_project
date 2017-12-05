$(document).ready(function() {
    $('.dropdown-hover').mouseover(function() {
      $('.dropdown-menu').show();
    });  
    $('.dropdown-hover').mouseleave(function() {
      $('.dropdown-menu').hide();
    });
});
