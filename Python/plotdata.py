import serial
import write
import Plotter
import matplotlib.animation as animation
import matplotlib.pyplot as plt

def parse(strdata):
    
    parseddata = [int(s) for s in str.split(strdata) if s.isdigit]
    return parseddata


teensy1 = write
try:
    ser = serial.Serial('/dev/ttyACM0',9600)
except:
    ser = serial.Serial('/dev/ttyACM1',9600)

     
   
index=0

while (ser.in_waiting == 0):
    pass

print "Serial Communication Setup"
textfilestr = raw_input("Type Number of File\n")
if (textfilestr == "0"):
    quit()
textfilenum = str(textfilestr)
file_path ="/home/debian/Desktop/PyScripts/DataFolder/Trial_" + textfilenum + "/filename.txt"
#teensy1.makedir(file_path)
#teensy1.DataFolder = "/home/debian/Desktop/PyScripts/DataFolder/Trial_" + textfilenum + "/"
ser.reset_input_buffer()
plt.ion()
while 1:
        
	data = ser.readline()
        
        array = parse(data)
    
        print "Data "
        print index
        index = index +1
        for idx, val in enumerate(array):
            print (idx,val)
        print data
       # write.appenddata("Data " + str(index) + ":\n",textfilenum)
       # teensy1.appenddata(data,textfilenum,"all")
        
        teensy1.appenddata(str(array[1]),textfilenum,"yellow")
        Plotter.animate(str(array[1]),textfilenum,"yellow")
        plt.show()
        plt.pause(0.05)
      #  teensy1.appenddata(str(array[1]),textfilenum,"blue")
      #  teensy1.appenddata(str(array[1]),textfilenum,"black")
      #  teensy1.appenddata(str(array[1]),textfilenum,"red")
      #  teensy1.appenddata(str(array[1]),textfilenum,"green")
      #  teensy1.appenddata(str(index),textfilenum,"time")
        
      #  teensy1.writedata(data,textfilenum,"all")
        
       # teensy1.writedata(str(array[0]),textfilenum,"yellow")
       # teensy1.writedata(str(array[1]),textfilenum,"blue")
       # teensy1.writedata(str(array[2]),textfilenum,"black")
       # teensy1.writedata(str(array[3]),textfilenum,"red")
       # teensy1.writedata(str(array[4]),textfilenum,"green")
       # teensy1.writedata(str(index),textfilenum,"time")
        ani = animation.FuncAnimation(Plotter.fig, Plotter.animate(str(array[1]),textfilenum,"yellow"), interval = 1000)
        
        
       

        
	
 
 