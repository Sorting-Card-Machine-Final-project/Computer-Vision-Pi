import gpoizero as gz
import serial

port = "dev/ttyS0" # Supposed to be the rught port for the pins
boudrate = 9600

ser = serial.Serial(port, baudrate)

def sendViaUART(tray, start, end, moreCards):
	data = 0x00
	
	# add handle to convert inputs to bits
	
	ser.write(bytes([data])
	
	ser.close() # check when do I need to do that