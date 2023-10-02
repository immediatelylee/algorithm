window.onload=function(){
// JavaScript로 동작 구현
const minusButton = document.getElementById("minus");
const plusButton = document.getElementById("plus");
const numberInput = document.getElementById("numberInput");

minusButton.addEventListener("click", () => {
    let currentValue = parseInt(numberInput.value);
    if (currentValue > 1) {
        currentValue--;
        numberInput.value = currentValue;
        if (currentValue === 1) {
            minusButton.disabled = true;
        }
    }
});

plusButton.addEventListener("click", () => {
    let currentValue = parseInt(numberInput.value);
    currentValue++;
    numberInput.value = currentValue;
    if (currentValue > 1) {
        minusButton.disabled = false;
    }
});
}