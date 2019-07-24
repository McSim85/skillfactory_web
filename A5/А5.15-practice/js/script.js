const grandpa = "Дед"
const grandma = "Баба"

$(document).ready(function() {
	$(".btn").click(function() {
		const result = $(".result");

		$.getJSON("https://api.myjson.com/bins/jcmhn", function (data) {
		  console.log(data.text);
		  data.text.var1 = "123"
		  //$(result).attr('var1', grandpa)
		  $(result).html('<p>' + data.text + '</p>');
		});
	});
});




