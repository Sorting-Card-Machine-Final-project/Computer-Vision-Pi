from  detect_model import card_detector
import time


def start_detection():
    print("Starting card detection...")
    card_detector_instance = card_detector.Card_Detector()
    detection = card_detector.detect_and_transmit(card_detector_instance)

    print(f"Detected cards: {detection}")
    return detection

def test_detections_continues(system_status):

    for _ in range(5):
        detection = start_detection()
        system_status["log"].append(f"detected: {detection}")
        system_status["deck_order"].append(detection)
        time.sleep(2)
