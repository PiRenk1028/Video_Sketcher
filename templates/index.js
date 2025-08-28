const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

canvas.width = 1000;
canvas.height = 1000;

function updateDisplay(){
  context.fillStyle = 'black';
  context.fillRect(0,0,canvas.width,canvas.height);
}

function loop(){
  window.requestAnimationFrame(loop);
  updateDisplay();

}


loop()
