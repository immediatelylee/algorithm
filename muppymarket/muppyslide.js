var slides = document.querySelector('.slides'),
slide = document.querySelectorAll('.slides li'),
currentIdx = 0,
slideCount = slide.length,
slideWidth = 1480,
slideMargin = 0
prevBtn = document.querySelector('.prev'),
nextBtn = document.querySelector('.next');

makeClone();

function makeClone(){
    for(var i = 0; i<slideCount;i++){
        var cloneSlide = slide[i].cloneNode(true);
        cloneSlide.classList.add('clone');
    }
}