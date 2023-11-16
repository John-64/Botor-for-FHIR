function sendMessage() {
    var userInput = document.getElementById("userInput");
    var chatBox = document.getElementById("chatBox");

    if (userInput.value.trim() !== "") {
        // User message
        var userMessage = document.createElement("div");
        userMessage.className = "message user-message";
        userMessage.innerHTML = "<strong>You:</strong> " + userInput.value;
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
