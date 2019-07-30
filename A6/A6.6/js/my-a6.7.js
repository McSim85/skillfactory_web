//function dummy(args) {
//	console.log(args);
//}
// let counter = 0

// function trackChecks() {
	// counter++
	// console.log(counter)
// }
// $("input[type=checkbox]:checked").change(trackChecks);

// function trackChecks() {
  // let checkCount = $("input[type=checkbox]:checked").length;
  // console.log(`Выбрано флажков: ${checkCount}`);
// }

const maxAllowedChecks = 2;

// function trackChecks() {
  // let checkCount = $("input[type=checkbox]:checked").length;
  // if (checkCount >= maxAllowedChecks) {
    // console.log("это много");
  // } else {
    // console.log("это нормально");
  // }
// }

// function trackChecks() {
  // let checkCount = $("input[type=checkbox]:checked").length;
  // if (checkCount >= maxAllowedChecks) {
    // $("input[type=checkbox]:not(:checked)").prop("disabled", true)
  // } else {
    // $("input[type=checkbox]:not(:checked)").prop("disabled", false);
  // }
// }

function trackChecks() {
  let checkCount = $("input[type=checkbox]:checked").length;
  $("input[type=checkbox]:not(:checked)").prop("disabled", checkCount >= maxAllowedChecks);
}

function trackRadios() {
  $("input[type=radio]").prop("disabled", true);
}

function init() {
  $("input[type=checkbox]").change(trackChecks);
  $("input[type=radio]").change(trackRadios);

  trackChecks(); 
 // trackRadios();
}

// function init() {

  // $("input[type=checkbox]").change(trackChecks);
// }

$(document).ready(init);
