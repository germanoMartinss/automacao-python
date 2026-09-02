import gradio as gr
from transformers import pipeline
from PIL import Image

def remove_background(image):
    pipeline_model = pipeline("image-segmentation", model="briaai/RMBG-1.4", trust_remote_code=True)
    pillow_mask = pipeline_model(image, return_mask=True)
    pillow_image = pipeline_model(image)
    return pillow_image

# remove_background("img/fefe.png")

app = gr.Interface(
    title="Remove Background",
    description="Faça upload de uma imagem e remova o fundo",
    fn=remove_background,
    inputs=gr.components.Image(type="pil"),
    outputs=gr.components.Image(type="pil", format="png"),
)
# if __name__ == "__main__":
app.launch(share=True)