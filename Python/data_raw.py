# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 20:45:58 2017

@author: debian
"""

import serial
import write


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

textfilenum = str(textfilestr)

ser.reset_input_buffer()

while 1:
        
	data = ser.readline()
        
        array = parse(data)
    
        print "Data "
        print index
        index = index +1
        for idx, val in enumerate(array):
            print (idx,val)
        print data
    #    teensy1.appenddata("Data " + str(index) + ":\n",textfilenum,"all")
        teensy1.appenddata(data,textfilenum,"all")
        
      #  teensy1.appenddata(str(array[1]),textfilenum,"yellow")
      #  teensy1.appenddata(str(array[1]),textfilenum,"blue")
      #  teensy1.appenddata(str(array[1]),textfilenum,"black")
      #  teensy1.appenddata(str(array[1]),textfilenum,"red")
      #  teensy1.appenddata(str(array[1]),textfilenum,"green")
      #  teensy1.appenddata(str(index),textfilenum,"time")
        
       
        
       

        
	
 
 