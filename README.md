# Google Voice UI with Secure API Proxy

This project demonstrates a UI with a rotating mic icon and a voice bar animation that triggers an API call to Google’s Generative Language API via a secure Flask proxy.

## Features

- **Flask backend** to securely proxy requests to the external API.
- **Client-side HTML, CSS, and JS** for the interactive UI.
- **Secure API key management:** The API key is stored server-side (or in environment variables) and is not exposed in client code.
- **CORS handling:** The Flask proxy ensures that CORS issues are managed.