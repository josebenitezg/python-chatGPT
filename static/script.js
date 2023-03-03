function showLoadingAnimation() {
    var userInput = document.getElementById("user-input");
    var submitBtn = document.getElementById("submit-btn");
  
    userInput.disabled = true;
    submitBtn.disabled = true;
    submitBtn.classList.add("loading");
  
    // Wait for 1 second before submitting the form
    setTimeout(function() {
      submitBtn.classList.remove("loading");
      userInput.disabled = false;
      submitBtn.disabled = false;
    }, 1000);
  }
  