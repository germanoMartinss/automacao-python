from transformers import DetrImageProcessor, DetrForObjectDetection
from PIL import Image, ImageDraw
import requests
import torch

url = 'http://images.cocodataset.org/val2017/000000039769.jpg'
image = Image.open(requests.get(url, stream=True).raw)

processor = DetrImageProcessor.from_pretrained('facebook/detr-resnet-101-dc5')
model = DetrForObjectDetection.from_pretrained('facebook/detr-resnet-101-dc5')

inputs = processor(images=image, return_tensors="pt")
outputs = model(**inputs)

# Só mantém detecções com confiança > 0.9
target_sizes = torch.tensor([image.size[::-1]])
results = processor.post_process_object_detection(outputs, target_sizes=target_sizes, threshold=0.9)[0]

draw = ImageDraw.Draw(image)

for score, label, box in zip(results["scores"], results["labels"], results["boxes"]):
    box = [round(i, 2) for i in box.tolist()]
    print(
        f"Detected {model.config.id2label[label.item()]} with confidence "
        f"{round(score.item(), 3)} at location {box}"
    )
    draw.rectangle(box, outline="red", width=3)
    draw.text((box[0], box[1]), model.config.id2label[label.item()])

image.show()
image.save("resultado_deteccao.jpg")
