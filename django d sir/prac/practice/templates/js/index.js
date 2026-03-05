console.log("✅ JS file linked correctly");

document.addEventListener("DOMContentLoaded", function () {
  const button = document.querySelector(".but");
  if (button) {
    button.addEventListener("click", function () {
      alert("✅ Thanks for clicking!");
      console.log("✅ Button clicked");
    });
  }
});
