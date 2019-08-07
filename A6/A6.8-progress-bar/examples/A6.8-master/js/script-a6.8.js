let currentProgress = 0;

function init() {
	setProgressBar(currentProgress);
}


$('#1').click(function(event) {
	incProgress(1)
});

$('#3').click(function(event) {
	incProgress(3)
});

$('#7').click(function(event) {
	incProgress(7);
});

function incProgress(increment) {
	currentProgress += increment;
	if (currentProgress > 100) {
		setProgressBar(100);
	}
	else {
		setProgressBar(currentProgress);
	}
}

function setProgressBar(number) {
	$('.progress-bar').css('width', number + '%').attr('aria-valuenow', number).text(number + '%');
} 

$(document).ready(init);