$(document).ready(init);
function init() {
	console.log('script downloaded')		
};

currentPr = $('#my-progress-bar').innerWidth();
var size=0; 

$(".btn1").click(function() {
	size = size+1;
	$("#my-progress-bar").width(size+'%');
	
	$mybar = $('#my-progress-bar');
	$mybar.html(size +'%');

});

var size=0; 

$(".btn3").click(function() {
	size = size+3;
	$("#my-progress-bar").width(size+'%');
	
	$mybar = $('#my-progress-bar');
	$mybar.html(size +'%');

});

$(".btn7").click(function() {
	size = size+7;
	$("#my-progress-bar").width(size+'%');
	
	$mybar = $('#my-progress-bar');
	$mybar.html(size +'%');

});
