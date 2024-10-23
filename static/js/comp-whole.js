// function to check the answer of the practice problem
        function checkAnswer(event) {
            event.preventDefault(); // prevent default form submission

            var comparisonSymbol = document.getElementById('comparisonSymbol').value.trim();
            var correctAnswer = '>';
            var feedback = document.getElementById('feedback');
            var inputField = document.getElementById('comparisonSymbol');
            var submitButton = document.getElementById('submitBtn');
            var finalForm = document.getElementById('final-form'); // form to submit once the answer is correct

            var allowedSymbols = ['>', '<', '='];

            // validate input
            if (allowedSymbols.indexOf(comparisonSymbol) === -1) {
                feedback.textContent = 'Invalid input. Please enter >, =, or <.';
                return;
            }

            // check for correct answer and provide feedback
            if (comparisonSymbol === correctAnswer) {
                feedback.textContent = 'Correct! 330 is greater than 280, so ">" is the correct symbol. Well done!';
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