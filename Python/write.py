# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 19:57:30 2017

@author: debian
"""
#write.py
#class file
import serial
import os

#function that splits a string into an array of integers
    #input: string (with numbers)
    #output: array of the numbers in the string
def parse(strdata):  
    parseddata = [int(s) for s in str.split(strdata) if s.isdigit]
    return parseddata

#global varibale assigned for Trial Number
textfilenum = 0

#class for every USB connectoin
class Connection:
    #establishes initial condictions of USB connection
    #will throw error is connection is not established
    def __init__(self,portnumber,USB):
        try:
            self.port = serial.Serial('/dev/tty' + str(USB),9600)
        except:
            raise Exception('Connection ' + str(portnumber) + " Failed")
        self.DataFolder = "/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/"
        self.FilePath ="/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/filename.txt"
        self.ConDataFolder = "/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/Connection_" + str(portnumber) + "/"  
        self.ConFilePath = "/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/Connection_" + str(portnumber) + "/filename.txt"         
        self.portnum = int(portnumber)
        
    #opens a directory/folder and creates or wrties to a file
        #inputs: string that needs to be written, number of given input, color is the name of sensor from which the datat is coming from
        #outputs: NONE
    def writedata(self,inputstring,number,color):
        filename = "Data_Trial_"+ str(color) + "_" + str(self.portnum) +".txt"
        f = open(os.path.join(self.ConDataFolder,filename),"a")
        f.write(inputstring + "\n")
        f.close()
    
    def appenddata(self,inputstring2,number,color):
        filename = "Data_Trial_"+ str(color) + "_"+ str(number) +".txt"
        f = open(filename,"a")
        f.write(inputstring2)
        f.close()
        
    #makes directory for Trial Folder based on FilePath
        #inputs: NONE
        #outputs: NONE
    def makedir(self):
        directory = os.path.dirname(self.FilePath)
        if not os.path.exists(directory):
            os.makedirs(directory)

    #makes directory for Connection Folder based on ConFilePath
        #inputs: NONE
        #outputs: NONE            
    def Conmakedir(self):
        directory = os.path.dirname(self.ConFilePath)
        if not os.path.exists(directory):
            os.makedirs(directory)
            
    #makes directory for Connection Folder based on ConFilePath
        #inputs: NONE
        #outputs: NONE    
    def setSer(self,connection):
        self.port = ('/dev/ttyACM' + str(connection),9600)
        
    #sets the path of the all folders and file locations based of Trial Number (textfilenum)
        #inputs: NONE
        #outputs: NONE         
    def setPath(self):
        self.DataFolder = "/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/"
        self.FilePath ="/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/filename.txt"
        self.ConDataFolder = "/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/Connection_" + str(self.portnum) + "/"  
        self.ConFilePath = "/home/debian/Desktop/Multi/PyScripts/DataFolder/Trial_" + str(textfilenum) + "/Connection_" + str(self.portnum) + "/filename.txt"         
        
    #sets the textfilnum to the Trial Number
        #inputs: integer
        #outputs: NONE     
    def setFileNum(self,TFN):
        global textfilenum
        textfilenum = TFN

    #sets the textfilnum to the Trial Number
        #inputs: integer
        #outputs: port of object         
    def getPort(self):
        return self.port
    
    #Records all the values in data and parses them to write them to individual files
        #inputs: sting data which needs to be parsed, integer index
        #outputs: NONE  
    def record(self,data,index):
        array = parse(data)
        self.writedata(data,textfilenum,"all")
        self.writedata(str(array[0]),textfilenum,"yellow")
        self.writedata(str(array[1]),textfilenum,"blue")
        self.writedata(str(array[2]),textfilenum,"black")
        self.writedata(str(array[3]),textfilenum,"red")
        self.writedata(str(array[4]),textfilenum,"green")
        self.writedata(str(index),textfilenum,"time")

    #reads input line from serial connection
        #inputs: NONE
        #outputs: string of data  
    def portRead(self):
        data = self.port.readline()
        return data

#if __name__ == '__main__':
    
        
    