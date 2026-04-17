# Azure GPT-4 Integration

This project allows you to interact with **Azure GPT-4** for generating text through a user-friendly interface powered by **Gradio**.

## Features:
- **GPT-4 Text Generation**: Enter a prompt and generate meaningful, contextually accurate text responses.
- **Gradio Interface**: Easily interact with Azure GPT-4 through a simple and clean web interface.

## Showcase:
<img src="assets/gpt-4.png" alt="Project Showcase" width="600px" />

## Requirements:
- Python 3.7+
- `openai` library
- `gradio` library
- `python-dotenv` library
- `azure-cli` installed for Azure deployment
- **API key** for **Azure GPT-4** from OpenAI or Azure platform.

## Setup Instructions:
1. Install dependencies:
    ```powershell
    py -m pip install openai gradio python-dotenv
    ```

2. Get API Keys:
    - To use **Azure GPT-4**, sign up for an account on [Azure](https://azure.microsoft.com/) or [OpenAI](https://platform.openai.com/) and generate an API key.
    - Create a `.env` file in the project root directory and add your API key, endpoint, and deployment name as follows:
        ```env
        API_KEY=your_openai_api_key_here
        GPT_ENDPOINT=https://<your-resource-name>.openai.azure.com
        GPT_DEPLOYMENT=gpt-5.4-nano
        ```
      
    - When publishing to Azure Web App, set these values as App Settings instead of committing `.env` to source control.

3. Run the app locally:
    ```powershell
    py chat.py
    ```

4. Open your browser and visit the provided URL to interact with the interface.

## How It Works:
- **GPT-4**: Takes a text prompt and provides a conversational AI response.

## Customizations:
- You can modify the temperature, max tokens, and other parameters for GPT-4 text generation to adjust the style and length of responses.

## Contributing:
Feel free to fork this repository, submit issues, and create pull requests for improvements.
