 function startCountdown(targetDate) {
  var countdown = setInterval(function() {
    var now = new Date().getTime();
    var distance = targetDate - now;

    var hours = Math.floor(distance / (1000 * 60 * 60));
    var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
    var seconds = Math.floor((distance % (1000 * 60)) / 1000);

    document.getElementById('hours').innerHTML = hours;
    document.getElementById('minutes').innerHTML = minutes;
    document.getElementById('seconds').innerHTML = seconds;

    if (distance < 0) {
      clearInterval(countdown);
      document.getElementById('countdown').innerHTML = 'Countdown finished!';
    }
  }, 1000);
}

// Set target date to 24 hours from now
var targetDate = new Date().getTime() + 24*60*60*1000;
startCountdown(targetDate);
