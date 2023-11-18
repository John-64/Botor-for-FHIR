function sendMessage() {
    var userInput = document.getElementById("userInput");
    var chatBox = document.getElementById("chatBox");

    if (userInput.value.trim() !== "") {
        // User message
        var userMessage = document.createElement("div");
        var userText = document.createElement("span");
        userMessage.className = "question-side";
        userText.className = "question-text";
        userText.innerHTML = userInput.value;
        userMessage.appendChild(userText);
        chatBox.appendChild(userMessage);

        // Bot response (you can customize this part)
        var botMessage = document.createElement("div");
        botMessage.className = "message bot-message";
        // Inserire qui la risposta del chatbot
        botMessage.innerHTML = "<strong>Bot:</strong> Thanks for your message!";
        chatBox.appendChild(botMessage);

        // Clear the input field
        userInput.value = "";

        // Scroll to the bottom of the chat box
        chatBox.scrollTop = chatBox.scrollHeight;
    }
}
