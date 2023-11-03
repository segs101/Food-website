const numberInput = document.getElementById("numberInput");
const incrementButton = document.getElementById("increment");
const decrementButton = document.getElementById("decrement");

incrementButton.addEventListener("click", () => {
  numberInput.stepUp();
});

decrementButton.addEventListener("click", () => {
  numberInput.stepDown();
});
