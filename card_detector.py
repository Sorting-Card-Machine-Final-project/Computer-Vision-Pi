from ultralytics import YOLO
import matplotlib.pyplot as plt
import cv2



class Card_Detector:

    def __init__(self, model="detect_model/best2.pt", t_interval=200, count_tresh=3, source=0):

        self.model = YOLO(model)
        self.time_interval = t_interval #the time to wait between each detection.
        self.count_tresh = count_tresh #used to validate a new card is visible and not just a glitch that identified a new card.
        self.source = source #camera mode or image.
        self.names = self.model.names #dictionary of all the cards id and string value.

    def get_detection_from_results(self, results):
        detections = set()
        for r in results:
            for c in r.boxes.cls:
                detections.add(self.names[int(c)])
        return detections
    
    def detect_card(self):
        # Capture frame from webcam
        cap = cv2.VideoCapture(self.source)
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture image")
            cap.release()
            return None
        
        # Process the frame
        results = self.model.predict(frame, conf=0.5, max_det=6, agnostic_nms=True, imgsz=640, task='detect')
        cap.release()
        
        detections = self.get_detection_from_results(results)
        
        if len(detections) > 0:
            detected_cards = []
            for detection in detections:
                detected_cards.append(detection)  # Extract the label of the detected card
            return detected_cards
        else:
            return None

    def detect_from_image(self, image):
        results = self.model.predict(image, conf=0.5, max_det=6, agnostic_nms=True, imgsz=640, task='detect')
        detections = self.get_detection_from_results(results)

        if len(detections) > 0:
            detected_cards = []
            for detection in detections:
                detected_cards.append(detection)  # Extract the label of the detected card
            return detected_cards
        else:
            return None

#TODO make sure len(detected cards) = 1/0
def detect_and_transmit(card_detector):
    detected_cards = card_detector.detect_card()
    if detected_cards:
        print(f"Detected Cards: {detected_cards}")
        return detected_cards[0]
    else:
        print("No card detected")
        return None
    
    

def transmit(card):
    print(f"Detected - {card}")

def main():
    card_detector = Card_Detector()
    last_card = None
    curr_card = None
    new_card_counter = 0
    while(True):
        curr_card = detect_and_transmit(card_detector)
        
        if(new_card_counter > 3):
            transmit(curr_card)
        
        if(last_card != curr_card):
            last_card = curr_card
            new_card_counter = 0
            continue
        
        if(last_card == curr_card):
            new_card_counter += 1




if __name__ == "__main__":
    main()

'''
result = results[0]

# Get the image with predictions
annotated_frame = result.plot()

# Display the image using Matplotlib
plt.imshow(annotated_frame)
plt.axis('off')  # Hide the axis
plt.show()
'''