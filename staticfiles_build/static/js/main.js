const numberInput = document.getElementById("numberInput");
const incrementButton = document.getElementById("increment");
const decrementButton = document.getElementById("decrement");

incrementButton.addEventListener("click", () => {
  numberInput.stepUp();
});

decrementButton.addEventListener("click", () => {
  numberInput.stepDown();
});


window.setTimeout(function () {
  $(".alert")
    .fadeTo(500, 0)
    .slideUp(500, function () {
      $(this).remove();
    });
}, 2000);