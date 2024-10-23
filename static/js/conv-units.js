 //method to check You Try answer
        function checkAnswer(event) {
            event.preventDefault(); // prevent default form submission

            var height = document.getElementById('height').value.trim();
            var correctAnswer = 228;
            var feedback = document.getElementById('feedback');
            var inputField = document.getElementById('height');
            var submitButton = document.getElementById('submitBtn');
            var finalForm = document.getElementById('final-form'); // form to submit once the answer is correct

            // check for correct answer and provide feedback
            if (parseInt(height) === correctAnswer) {
                feedback.textContent = 'Correct! A foot is made up of 12 inches, so we multiply 19 * 12 = 228 inches. Well done!';
                inputField.disabled = true; // disable input field
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