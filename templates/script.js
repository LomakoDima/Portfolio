const textElement = document.querySelector(".sec-text");
const words = ["Freelancer", "WEB DEVELOPER", "PYTHON DEVELOPER", "JAVA DEVELOPER", "GAME DEVELOPER"];
let wordIndex = 0;

function typeText() {
    textElement.style.width = '0';  // Reset the width before typing next text
    textElement.textContent = words[wordIndex];
    textElement.style.animation = 'none'; // Reset animation
    setTimeout(() => {
        textElement.style.animation = ''; // Apply animation
    }, 0);

    wordIndex = (wordIndex + 1) % words.length;  // Cycle through words
}


typeText();
setInterval(typeText, 4000);  // Adjust timing based on your preference
