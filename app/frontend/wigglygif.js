// JavaScript Document
  $(document).ready(function(){
	  
	$('#home').click(function()
	{
		$('section').removeClass('active-page');
	});
  	$('#about').click(function()
	{
		$('.about').toggleClass('active-page');
		$('#about i').slideToggle();
		$('#about p').fadeToggle();	
	});
	$('#contact').click(function()
	{
		$('.contact').toggleClass('active-page');
		$('#contact i').slideToggle();
		$('#contact p').fadeToggle();
	});
  });
  $(function() {
    $( document ).tooltip({
      track: true
    });
  });