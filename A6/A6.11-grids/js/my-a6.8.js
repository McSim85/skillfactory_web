let sourcePercent = 0
let currentPercent = sourcePercent
let maxPercent = 100

function increasePercent(src, inc) {
	return src + inc;
	// final = ;
	// if ( final >= max ) {
		// final -=  max;
		// console.log( max - final );
		// //return max - final;
	// } else {
		// console.log( final );
		// //return final;
	// }
}

// function increaseOne () {
	// console.log('one');
// }

// function increaseThree () {
	// console.log('Three');
// }

// function increaseSeven () {
	// console.log('Seven');
// }

function main() {
	//console.log("Main");
	$('.btn-dark').click( function() {
		currentPercent = increasePercent(currentPercent, 1);
		let elem = document.querySelector('#my-progress-bar');
		// Set the height to currentPercent
		elem.style.width = currentPercent + "%";
	});
	$('.btn-primary').click( function() {
		currentPercent = increasePercent(currentPercent, 3);
		let elem = document.querySelector('#my-progress-bar');
		// Set the height to currentPercent
		elem.style.width = currentPercent + "%";
	});
	$('.btn-danger').click( function() {
		currentPercent = increasePercent(currentPercent, 7);
		let elem = document.querySelector('#my-progress-bar');
		// Set the height to currentPercent
		elem.style.width = currentPercent + "%";
	});
	
	// why doesn't it work?
	// $('.btn-dark').click(increaseOne ());
	// $('.btn-primary').click(increaseThree ());
	// $('.btn-danger').click(increaseSeven ());
};

$(document).ready(main);
