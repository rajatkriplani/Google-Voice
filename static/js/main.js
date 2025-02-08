// static/js/main.js

document.addEventListener("DOMContentLoaded", function () {
  const micButton = document.querySelector(".micButton");
  const container = document.querySelector(".googleVoiceContainer");

  micButton.addEventListener("click", () => {
    // Toggle the active class to start the CSS animations
    container.classList.toggle("active");

    // For now, we are using a static text prompt. In a real chat bot, you might gather input from a text box.
    const promptText = "Explain how AI works";

    // Send the prompt to the Flask backend endpoint
    fetch("/api/generate", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text: promptText }),
    })
      .then((response) => response.json())
      .then((data) => {
        console.log("API Response:", data);
        // Display the API response in the chat window
        const chatWindow = document.getElementById("chat-window");
        const messageElem = document.createElement("div");
        messageElem.className = "chat-message";
        // For demonstration, we display the raw JSON. Adjust as needed.
        messageElem.textContent = JSON.stringify(data, null, 2);
        chatWindow.appendChild(messageElem);
      })
      .catch((error) => {
        console.error("Error calling API:", error);
      });
  });
});