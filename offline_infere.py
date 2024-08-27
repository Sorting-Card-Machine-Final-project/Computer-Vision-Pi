'''from ultralytics import YOLO

# Load the model
model = YOLO("card_detector.pt")  # Ensure this points to your model file

# Perform inference
results = model("test.PNG")  # Replace with your test image

print(results)
'''
from ultralytics import YOLO
import matplotlib.pyplot as plt

# Load the model
model = YOLO("best2.pt")  # Ensure this points to your model file

# Perform inference
results = model(source=0, conf=0.5, max_det=6, agnostic_nms=True, show=True, imgsz=640, task='detect')  # Replace with your test image

# Access the first (and only) result
result = results[0]

# Get the image with predictions
annotated_frame = result.plot()

# Display the image using Matplotlib
plt.imshow(annotated_frame)
plt.axis('off')  # Hide the axis
plt.show()
