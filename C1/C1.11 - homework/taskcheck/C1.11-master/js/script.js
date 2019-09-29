class CountDown{

    constructor(){
      this.reset()
    }
  
    reset(){
      this.minutes = 0;
      this.seconds = 0;
      this.setValues();
      $('.pause').hide();
      $('.start').show();    
    }
  
    setValues(){
      $('.minutes').value((0 + String(this.minutes)).slice(-2));
      $('.seconds').value((0 + String(this.seconds)).slice(-2));
    }
  
    incMinutes(){
      if(this.minutes < 59) ++this.minutes;
      this.setValues(); 
    }
  
    incSeconds(){
      if(this.seconds < 59) {++this.seconds}
      else if (this.minutes < 59){
        ++this.minutes 
        this.seconds = 0;
      }
      this.setValues();
    }
  
    decMinutes(){
      if(this.minutes > 0) --this.minutes;
      this.setValues();
    }
  
    decSeconds(){
      if(this.seconds > 0){--this.seconds}
      else if(this.minutes > 0){
        this.seconds = 59;
        --this.minutes;
      }
      this.setValues();
    }
  
    start(){
      $('.start').hide();
      $('.pause').show();
      let total = 0 + this.seconds + this.minutes * 60;
      this.timeinterval = setTimeout(this.start.bind(this), 1000);
      if(total <= 0){
        clearInterval(this.timeinterval);
        $('.countdown').hide();
        $('.countdown-legend').hide();
        $('.control').hide();
        $('.restart').show();
        $('.message').html('<h1>завершил работу!</h1>');
      }
      if(this.seconds > 0) --this.seconds
      else{
        this.seconds = 59;
        --this.minutes;
      }
      this.setValues();
    }
  
    pause(){
      clearInterval(this.timeinterval);
      $('.pause').hide();
      $('.start').show();
    }
  }
  
  
  timer = new CountDown();
  
  $('.start').click(() => timer.start());
  
  $('.pause').click(() => timer.pause());
  
  $('.seconds').change(() => {
    let val = parseInt($('.seconds').value(), 10);
    if((Number.isNaN(val)) || (val < 0) || (val > 59)){
      alert("Введите число от 0 до 59.");
    }
    else timer.seconds = val; 
    timer.setValues();
  });
  
  $('.minutes').change(() => {
    let val = parseInt($('.minutes').value(), 10);
    if((Number.isNaN(val)) || (val < 0) || (val > 59)){
      alert("Введите число от 0 до 59.");
    }
    else timer.minutes = val; 
    timer.setValues();
  });
  
  $('.minutes-minus').click(() => timer.decMinutes());
  
  $('.minutes-plus').click(() => timer.incMinutes());
  
  $('.seconds-minus').click(() => timer.decSeconds());
  
  $('.seconds-plus').click(() => timer.incSeconds());
  
  $('.restart').click(()=>{
    timer.reset();
    $('.countdown').show();
    $('.countdown-legend').show();
    $('.control').show();
    $('.message').html('');
    $('.restart').hide();
  }).hide();
  