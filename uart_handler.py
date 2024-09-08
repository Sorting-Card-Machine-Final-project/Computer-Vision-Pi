import time
#import serial  # This will be used on Raspberry Pi for UART communication

# Simulating UART communication
def send_command(command):
    print(f"Sending command to STM: {command}")
    # Uncomment this when running on the Raspberry Pi
    # with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
    #     ser.write(command.encode())
    time.sleep(1)
    return f"Command '{command}' sent to STM"

# Simulated response from STM
def receive_response():
    # Placeholder for reading response
    # with serial.Serial('/dev/ttyS0', 9600, timeout=1) as ser:
    #     response = ser.readline().decode()
    response = "Simulated STM response"
    print(response)
    return response
