document.addEventListener('DOMContentLoaded', () => {
    const micButton = document.querySelector('.micButton');
    const container = document.querySelector('.googleVoiceContainer');
  
    micButton.addEventListener('click', () => {
      // Toggle active class to start animations
      container.classList.toggle('active');
  
      // Call your Flask backend which proxies the request to the external API
      fetch('/api/generate-content', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          contents: [{
            parts: [{ text: "Explain how AI works" }]
          }]
        })
      })
      .then(response => {
        if (!response.ok) {
          throw new Error("Network response was not ok: " + response.statusText);
        }
        return response.json();
      })
      .then(data => {
        console.log("API Response:", data);
        // Optionally, update the UI with the returned content
      })
      .catch(error => {
        console.error("Error calling API:", error);
      });
    });
  });  