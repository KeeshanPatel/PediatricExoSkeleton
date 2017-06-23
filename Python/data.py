#data.py
    #main script
import write
import subprocess
from time import sleep

#Prompts userhow many connectiosn there are
    #checks if entry is a number 
    #Casts input as integer
a = False
while a == False:
    coms = raw_input("How many connections are there? ")
    if (coms.isdigit() == False):
        print "That is not a valid number\n"
    else:
        a = True
        coms = int(coms)
        
#A linux Bash script is called
    #USBlist.sh lists all the attached USB deviced and the dev/ port that they are attached to 
print "\n"
subprocess.call("USBlist.sh")

#Prompts user to enter all the connections via usb
    #declared Connection array, each elemetns is created and added to array
connections = []
for x in range(0,coms):
    USB = raw_input("What is the connection #" + str(x) + "'s name? (Type letters after the '/tty'\n")
    connections.append(write.Connection(x,USB))

#Prompts user to type in the trial number
    #checks to see if entered was integer or not
    #passed value to global varibale textfilnum which is used for naming files and creating directories
print "\n"
a = False
while a == False:
    textfilestr = raw_input("Type Trial Number (Type 'stop' to exit)\n")
    if (textfilestr == "stop"):
        quit()
    if (textfilestr.isdigit() == False):
        print "That is not a valid number\n"
    else:
        a = True
write.textfilenum = int(textfilestr)

#Traverses array to set up connections
    #resets each serial connection so a clean start can be made
    #clears the buffer of each serial connection
    #waits for serial communication to start
for x in range(0,coms):
    connections[x].getPort().reset_input_buffer()
    connections[x].getPort().setDTR(False)
    sleep(1)
    connections[x].getPort().flushInput()
    connections[x].getPort().setDTR(True)
    while (connections[x].getPort().in_waiting == 0):
        pass
    print "Connection " + str(x) + " has been successfully established"
print "Serial Communication Setup\n"

#Promts user to start and notifies user hwo to exit (Control+c)
raw_input("Press Enter to Start or Type 'stop' to exit\n During trial press control + c to stop")
if (textfilestr == "0"):
        quit()

#Traverses connections array to make all directories and set the dataFolder Path
    #creates both Trial folder and Connections Folder        
for x in range(0,coms):
    connections[x].setPath()
    connections[x].makedir()
    connections[x].Conmakedir()
    connections[x].getPort().reset_input_buffer()

#main loop
    #traverses connection array and reads the port and passes value to record function
    #keeps track of index value
index=0
while 1:
    for x in range(0,coms):
        data = connections[x].portRead()
        connections[x].record(data,index)   
        print str(data) + "Connection: " + str(x)
   
    print index
    index = index +1
        
       
     
        
       

        
	
 
 