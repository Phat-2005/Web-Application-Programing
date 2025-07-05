const images = ["img.png", "TFONE.jpg", "transformers-one-web.jpg"];
let index = 0;
const imgEl = document.getElementById("slide");

function showImage(i) {
  index = (i + images.length) % images.length;
  imgEl.src = images[index];
}

function next() { showImage(index + 1); }
function prev() { showImage(index - 1); }

setInterval(() => next(), 3000);
