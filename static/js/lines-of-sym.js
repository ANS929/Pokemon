// function to check the You Try answer
        function checkAnswer(event) {
            event.preventDefault(); // prevent default form submission

            var selectedOption = document.querySelector('input[name="TF"]:checked');
            var feedback = document.getElementById('feedback');
            var submitButton = document.getElementById('submitBtn');
            var finalForm = document.getElementById('final-form'); // form to submit once the answer is correct

            if (!selectedOption) {
                feedback.textContent = 'Please select an answer.';
                return;
            }

            var selectedValue = selectedOption.value;
            var correctAnswer = 'true';

            if (selectedValue === correctAnswer) {
                feedback.textContent = 'Correct! All 3 symbols have vertical symmetry. We can imagine folding each symbol in half, and its left side would match its right side exactly. Well done!';
                submitButton.disabled = true; // disable submit button
                finalForm.style.display = 'block'; // show the final submission form
            } else {
                feedback.textContent = 'Incorrect. Please try again.';
            }
        }

        // Function to handle popup image display (for cards)
        document.querySelectorAll(".image img").forEach(image => {
            image.onclick = () => {
                document.querySelector(".popup-image").style.display = "block";
                document.querySelector(".popup-image img").src = image.getAttribute("src");
            };
        });

        // Close the popup when clicking outside the image (for cards)
        document.querySelector(".popup-image").onclick = (event) => {
            if (event.target.classList.contains('popup-image')) {
                document.querySelector(".popup-image").style.display = "none";
            }
        };

        // Function to handle popup image display (for symbols)
        document.querySelectorAll(".image2 img").forEach(image => {
            image.onclick = () => {
                document.querySelector(".popup-image2").style.display = "block";
                document.querySelector(".popup-image2 img").src = image.getAttribute("src");
            };
        });

        // Close the popup when clicking outside the image (for symbols)
        document.querySelector(".popup-image2").onclick = (event) => {
            if (event.target.classList.contains('popup-image2')) {
                document.querySelector(".popup-image2").style.display = "none";
            }
        };