import gradio as gr
from model import GeminiModel

def create_interface():
    model = GeminiModel()
    
    def process_input(message, history):
        response = model.generate_response(message)
        return {"role": "assistant", "content": response}

    css = """
    body {background-color: #f5e6d3;}
    .message {color: black !important;}
    .footer {text-align: center; color: black; padding: 10px;}
    """
    
    chatbot = gr.ChatInterface(
        fn=process_input,
        title="Gemini Chatbot",
        description="Chat with Gemini AI",
        theme=gr.themes.Soft(
            primary_hue="neutral",
            secondary_hue="neutral",
            neutral_hue="neutral",
        ),
        css=css
    )
    
    footer = gr.HTML("<div class='footer'>© Iqbal M 2024</div>")
    
    with gr.Blocks(css=css, theme=gr.themes.Soft(
            primary_hue="neutral",
            secondary_hue="neutral",
            neutral_hue="neutral"
        )) as demo:
        
        chatbot.render()
        footer.render()

    return demo
