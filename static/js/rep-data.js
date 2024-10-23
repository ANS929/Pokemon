// function to check the answer for You Try problem
        function checkAnswer(event) {
            event.preventDefault(); // prevent default form submission

            var selection = document.getElementById('selection').value;
            var correctAnswer = 'False';
            var feedback = document.getElementById('feedback');
            var selectField = document.getElementById('selection');
            var submitButton = document.getElementById('submitBtn');
            var finalForm = document.getElementById('final-form'); // form to submit once the answer is correct

            // check for correct answer and provide feedback
            if (selection === correctAnswer) {
                feedback.textContent = 'Correct! A bar graph is used to compare items, so we could use it to compare the amounts of each type of deck. Well done!';
                selectField.disabled = true; // disable select field
                submitButton.disabled = true; // disable submit button
                finalForm.style.display = 'block'; // show the final submission form
            } else {
                feedback.textContent = 'Incorrect. Please try again.';
            }
        }

        // Function to handle popup image display
        document.querySelectorAll(".image img").forEach(image => {
            image.onclick = () => {
                document.querySelector(".popup-image").style.display = "block";
                document.querySelector(".popup-image img").src = image.getAttribute("src");
            };
        });

        // Close the popup when clicking outside the image
        document.querySelector(".popup-image").onclick = (event) => {
            if (event.target.classList.contains('popup-image')) {
                document.querySelector(".popup-image").style.display = "none";
            }
        };