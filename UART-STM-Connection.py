import gpoizero as gz
import serial

# port = "dev/ttyS0" # Supposed to be the right port for the pins
# boudrate = 9600

# ser = serial.Serial(port, baudrate)

# def sendViaUART(tray, start, end, moreCards):
# 	data = 0x00
	
# 	#tray is a number between 1 to 4 and has 2 bits
# 	data = data | bin(tray - 1)
	
# 	if start > 0:
# 		data = data | 0b100
# 	if end > 0:
# 		data = data | 0b1000
# 	if moreCards > 0:
# 		data = data | 0b10000
		
	
# 	# add handle to convert inputs to bits
	
# 	ser.write(bin(data))
	
# 	ser.close() # check when do I need to do that


class UARTSend:
	def __init__(self):
		port = "dev/ttyS0" # Supposed to be the right port for the pins
		boudrate = 9600
		self.ser = serial.Serial(port, boudrate)

	def sendViaUART(self, tray, start, end, moreCards):
		data = 0x00
		
		#tray is a number between 1 to 4 and has 2 bits
		data = data | bin(tray - 1)
		
		if start > 0:
			data = data | 0b100
		if end > 0:
			data = data | 0b1000
		if moreCards > 0:
			data = data | 0b10000
			
		
		# add handle to convert inputs to bits
		
		self.ser.write(bin(data))
		
		self.ser.close() # check when do I need to do that