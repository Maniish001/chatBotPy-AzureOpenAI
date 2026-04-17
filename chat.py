from openai import OpenAI
import gradio as gr
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = os.getenv("GPT_ENDPOINT")
DEPLOYMENT_NAME = os.getenv("GPT_DEPLOYMENT")

if not API_KEY or not BASE_URL or not DEPLOYMENT_NAME:
    raise ValueError(
        "Missing required .env values. Make sure API_KEY, GPT_ENDPOINT, and GPT_DEPLOYMENT are set."
    )

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)


def chat_with_gpt(prompt):
    try:
        response = client.chat.completions.create(
            model=DEPLOYMENT_NAME,
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": prompt},
            ],
            temperature=0.7,
            top_p=0.95,
            max_completion_tokens=800,
        )
        message = response.choices[0].message
        if hasattr(message, "content"):
            return message.content
        if isinstance(message, dict):
            return message.get("content", "")
        return str(message)
    except Exception as e:
        return f"Error: {str(e)}"


# Gradio Interface for GPT-4
def generate_response(prompt):
    text_response = chat_with_gpt(prompt)
    return text_response


# Gradio interface setup
with gr.Blocks(
    css="""
.gradio-container {
    background-color: #2d3436;
    color: #dfe6e9;
    font-family: 'Arial', sans-serif;
    display: flex;
    flex-direction: column;
    justify-content: flex-start;
    align-items: center;
    padding: 40px;
    box-sizing: border-box;
    height: 100vh;
    overflow-y: auto;
}

.gradio-markdown {
    text-align: center;
    color: #74b9ff;
    font-size: 32px;
    font-weight: bold;
    margin-bottom: 30px;
    width: 100%;
}

.gradio-input, .gradio-textbox {
    background-color: #34495e;
    border: 1px solid #7f8c8d;
    border-radius: 10px;
    color: #dfe6e9;
    font-size: 16px;
    padding: 15px;
    width: 100%;
    max-width: 600px;
    margin-bottom: 15px;
    height: 50px;
    box-sizing: border-box;
}

.gradio-input:focus, .gradio-textbox:focus {
    border-color: #74b9ff;
    outline: none;

.gradio-button {
    background-color: #74b9ff;
    border: none;
    color: white;
    font-size: 18px;
    padding: 15px;
    border-radius: 10px;
    cursor: pointer;
    width: 100%;
    max-width: 600px;
    margin-bottom: 30px;
    transition: background-color 0.3s ease;
}

.gradio-button:hover {
    background-color: #0984e3;
}

.gradio-button:active {
    background-color: #016aa7;
}

.gradio-image {
    width: 100%;
    height: auto;
    border-radius: 10px;
    border: 1px solid #7f8c8d;
    max-width: 600px;
    margin-top: 20px;
}

.gradio-tab {
    background-color: #74b9ff;
    color: white;
    border-radius: 8px;
    padding: 12px;
    font-weight: bold;
    margin: 10px;
}

.gradio-tab.selected {
    background-color: #0984e3;
}

.gradio-row {
    margin-bottom: 20px;
}
"""
) as demo:
    gr.Markdown("# Azure GPT-4 Text Generator")
    gr.Markdown(
        "Enter a prompt to interact with Azure GPT-4 and receive a text response."
    )

    # Section for GPT-4 Text Generation
    with gr.Tab("GPT-4 Text Generation"):
        with gr.Row():
            prompt_gpt = gr.Textbox(
                label="Enter your prompt", placeholder="e.g., Tell me a joke!", lines=2
            )
            generate_button_gpt = gr.Button("Generate Text Response")
        with gr.Row():
            output_message = gr.Textbox(label="GPT-4 Response", interactive=False)
        generate_button_gpt.click(
            generate_response, inputs=prompt_gpt, outputs=output_message
        )

# Launch the interface
if __name__ == "__main__":
    demo.launch(
        server_name="0.0.0.0",
        server_port=int(os.environ.get("PORT", 8000)),
        share=False,
    )
