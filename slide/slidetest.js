const slider = document.querySelector('.slider');
const images = document.querySelectorAll('.slider img');
const pauseButton = document.getElementById('pause');
const prevButton = document.getElementById('prev');
const pagination = document.getElementById('pagination');
const nextButton = document.getElementById('next');
let currentSlide = 0;
let isPlaying = true;

function updatePagination() {
  pagination.textContent = `${currentSlide + 1}/${images.length}`;
}

function pauseSlider() {
  isPlaying = false;
  pauseButton.textContent = '▶';
}

function playSlider() {
  isPlaying = true;
  pauseButton.textContent = '||';
  animateSlider();
}

function animateSlider() {
  if (isPlaying) {
    currentSlide = (currentSlide + 1) % images.length;
    updatePagination();
    slider.style.transform = `translateX(-${currentSlide * 100}%)`;
  }
}

pauseButton.addEventListener('click', () => {
  if (isPlaying) {
    pauseSlider();
  } else {
    playSlider();
  }
});

prevButton.addEventListener('click', () => {
  currentSlide = (currentSlide - 1 + images.length) % images.length;
  updatePagination();
  slider.style.transform = `translateX(-${currentSlide * 100}%)`;
});

nextButton.addEventListener('click', animateSlider);

updatePagination();
setInterval(animateSlider, 2000); // Auto-play every 2 seconds