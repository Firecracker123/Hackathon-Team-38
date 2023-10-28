console.log("Loaded image.js!");

const canv = document.getElementById("canvas");

// borrowed from https://stackoverflow.com/questions/10214873/make-canvas-as-wide-and-as-high-as-parent
function fitToContainer(canvas) {
    // Make it visually fill the positioned parent
    canvas.style.width ='100%';
    canvas.style.height='100%';
    // ...then set the internal size to match
    canvas.width  = canvas.offsetWidth;
    canvas.height = canvas.offsetHeight;
}
fitToContainer(canv);

const ctx = canv.getContext("2d");

const current_img = new Image();
const audio = new Audio("/static/soundtrack.mp3")

function draw() {
    // the idea is to read in here the current url value from a
    // hidden HTML element which will be modified by the game logic in python

    current_url = document.getElementById("current_url")

    fetch('/imageurl')
                .then(response => response.text())
                .then(data => {
                    console.log(data)
                    current_img.src = data
                });

    ctx.drawImage(current_img, 0, 0, canv.width, canv.height);
    requestAnimationFrame(draw);
}

requestAnimationFrame(draw);