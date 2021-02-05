pauseButton = document.querySelector('.pause');
nextButton = document.querySelector('.play-next');
previousButton = document.querySelector('.play-previous');
click = new Audio('/static/Event/click.wav');
pause = true;
pauseButton.addEventListener('click', clickplay=>{
  click.play();
  if(pause == true){
    console.log("Resume")
    document.getElementById('pause').style.backgroundImage="url('/static/img/play.png')";
    pause = false;
}
else{
    document.getElementById('pause').style.backgroundImage="url('/static/img/pause.png')";
    console.log("Pause");
    pause = true;
  }
})
nextButton.addEventListener('click', clickskip=>{
  click.play();
})
previousButton.addEventListener('click', clickskip=>{
  click.play();
})
