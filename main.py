import gradio as gr

# Launches a hello world gradio app on port 8080
with gr.Blocks() as demo:
    gr.Markdown("# Hello World")

demo.launch(server_port=8080)
