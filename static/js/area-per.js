var question1Correct = false;
        var question2Correct = false;

        // Question 1 logic (area)
        function checkAnswer1(event) {
            event.preventDefault(); // prevent default form submission

            var area = document.getElementById('area').value.trim();
            var correctAnswer = 2196;
            var feedback = document.getElementById('feedback1');
            var inputField = document.getElementById('area');
            var submitButton = document.getElementById('submitBtn1');

            // check for correct answer and provide feedback
            if (parseInt(area) === correctAnswer) {
                feedback.textContent = 'Correct! Area is length times width, so 61 * 36 = 2196 square centimeters. Well done!';
                inputField.disabled = true; // disable input field
                question1Correct = true; // mark question 1 as correct
                submitButton.disabled = true; // disable submit button

                // check if both questions are answered correctly
                checkFinalSubmission();
            } else {
                feedback.textContent = 'Incorrect. Please try again.';
                question1Correct = false; // mark question 1 as incorrect
            }
        }

        //Question 2 logic (perimeter)
        function checkAnswer2(event) {
            event.preventDefault(); // prevent default form submission

            var perimeter = document.getElementById('perimeter').value.trim();
            var correctAnswer = 194;
            var feedback2 = document.getElementById('feedback2');
            var inputField = document.getElementById('perimeter');
            var submitButton = document.getElementById('submitBtn2');

            // check for correct answer and provide feedback
            if (parseInt(perimeter) === correctAnswer) {
                feedback2.textContent = 'Correct! Perimeter is two times the length plust two times the width, so 2*61 + 2*36 = 122 + 72 = 194 centimeters. Well done!';
                inputField.disabled = true; // disable input field
                submitButton.disabled = true; // disable submit button
                question2Correct = true; // mark question 2 as correct

                // check if both questions are answered correctly
                checkFinalSubmission();
            } else {
                feedback2.textContent = 'Incorrect. Please try again.';
                question2Correct = false; // mark question 2 as incorrect
            }
        }

        // function to check if both questions are answered correctly for final submission
        function checkFinalSubmission() {
            var finalForm = document.getElementById('final-form');

            // enable final submission button if both questions are correct
            if (question1Correct && question2Correct) {
                finalForm.style.display = 'block';
            } else {
                finalForm.style.display = 'none';
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