from flask import Flask, render_template, jsonify, request
import uart_handler 
import gpio_control 
import image_detection 

app = Flask(__name__)


system_status = {"log": [], "running": False, "deck_order": []}


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_process', methods=['POST'])
def start_process():
    global system_status
    detection = None
    if not system_status["running"]:
        system_status["running"] = True
        system_status["log"].append("Process started.")

    #detection = image_detection.start_detection() #for single detection
    #system_status["log"].append(detection) 
    #system_status["deck_order"].append(detection)
    image_detection.test_detections_continues(system_status)
    # call main process function here:
    
    # gpio_control.activate_motors()
    # uart_handler.send_command('START')
    # cv_logic.start_detection()

    return jsonify({"status": "Process initialized"})

# API to stop process (or reset)
@app.route('/stop_process', methods=['POST'])
def stop_process():
    global system_status
    if system_status["running"]:
        system_status["running"] = False
        system_status["log"].append("Process stopped.")
        # gpio_control.deactivate_motors()
        # uart_handler.send_command('STOP')

    return jsonify({"status": "Process stopped"})

# API to show logs
@app.route('/get_logs', methods=['GET'])
def get_logs():
    global system_status
    return jsonify(system_status["log"])

@app.route('/get_deck_order', methods=['GET'])
def get_deck_order():
    return jsonify(system_status["deck_order"])


if __name__ == '__main__':
    # Run Flask app for testing on localhost (debug mode)
    app.run(debug=True, host='0.0.0.0')
