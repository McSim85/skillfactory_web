function handleButton1() {
    /* перевести цифры в проценты */ 
    const currentProgress = $('#my-progress-bar1').width(); // число
    const stepProgress = 1;
    const finalProgress = currentProgress *(1 + stepProgress / 100);

    $('#my-progress-bar1').width(finalProgress);
};

function handleButton2() {
    const currentProgress = $('#my-progress-bar2').width(); // число
    const stepProgress = 3;
    const finalProgress = currentProgress *(1 + stepProgress / 100);

    $('#my-progress-bar2').width(finalProgress);
};

function handleButton3() {
    const currentProgress = $('#my-progress-bar3').width(); // число
    const stepProgress = 7;
    const finalProgress = currentProgress *(1 + stepProgress / 100);

    $('#my-progress-bar3').width(finalProgress);
};

function init() {

        $("#my-button1").click(function() {
            handleButton1()
        });

        $("#my-button2").click(function() {
            handleButton2()
        });

        $("#my-button3").click(function() {
            handleButton3()
        });


}

$(document).ready(init);