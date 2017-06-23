
import serial 

ser = serial.Serial('/dev/ttyACM0',9600)

while 1:
	data = ser.readline()
        print data
        array = [int(s) for s in str.split(data) if s.isdigit]
        print array[0]
        print array[1]
	print "test"






