function checkAnswer(event) {
            event.preventDefault(); // prevent default form submission

            var notTrainers = document.getElementById('notTrainers').value;
            var correctAnswer = '2/5';
            var feedback = document.getElementById('feedback');
            var selectField = document.getElementById('notTrainers');
            var submitButton = document.getElementById('submitBtn');
            var finalForm = document.getElementById('final-form'); // form to submit once the answer is correct

            // check for correct answer and provide feedback
            if (notTrainers === correctAnswer) {
                feedback.textContent = 'Correct! 36/60 cards are Trainers, so 60/60 - 36/60 = 24/60 are not. 24/60 reduces to 2/5 since both 24 and 60 are divisble by 12. Well done!';
                selectField.disabled = true; // disable input field
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