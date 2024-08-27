import roboflow
from ultralytics import YOLO

# Replace 'YOUR_API_KEY' and 'YOUR_PROJECT_ID' with your actual Roboflow API key and project ID
rf = roboflow.Roboflow(api_key="OWScDyirh9SRloXM4K5m")
project = rf.workspace("kuper").project("card-detection-zk7wu-gzidp")

# Download the dataset (this step is done online)
dataset = project.version("1").download("yolov8")

# Load the model
model = YOLO("best2.pt")  # Replace with your actual model file name

# Perform any inference (optional)
results = model("test.PNG")  # Replace with an actual image
print(results)

# Save the model locally for offline use
model.export()
