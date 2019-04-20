# coding: utf-8

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy
import PIL
import serial
from serial import Serial
import time 
from time import sleep

#t=0
port1 = '/dev/ttyACM1'
speed = 9600
port2 = '/dev/ttyACM0'
speed2 = 9600

arduinoData1 = serial.Serial(port1,speed)
#time.sleep(2)
#print("Connection to " + port1 + " established succesfully!\n")
arduinoData2 = serial.Serial(port2,speed2)
 
# Convert PIL Image to NumPy array

from PIL import Image

image = Image.open("tiger.png")
img = image.resize((210,118))

img2 = img


arr = numpy.array(img)
#arr = arr[10:20,10:20,:]
#print(arr[0,0,0])
arrayOfInverted=[]
imn=[[],[],[]]
a = []
b=[]

# Convert array to Image

img = PIL.Image.fromarray(arr)

for i in range(arr.shape[2]):
    im=arr[:,:,i]
    for j in range(im.shape[0]):
        for k in range(im.shape[1]):
           # im[j][k]=255-im[j][k]
	  # print(im[j][k])
	  #  print(\n)
            string = str(int(im[j][k]))+ '\n'
	    arduinoData1.write(string.encode())
	  
	    
	    ms=arduinoData2.readline()
	    sleep(.001)
	    msg=str(ms.decode("utf-8"))
	    
	    zz=int(msg)
	    
	    print(im[j][k],zz,j,k )
	    #im[j][k] = 255-im[j][k]
	    im[j][k] = zz
	    #sleep(.001)
    arr[:,:,i]=im[:,:]
      
	    
	    #print(\n)

plt.imshow(arr)
plt.savefig("inverted_tiger.jpg")

#plt.imshow(img2)
#plt.savefig("6_1.jpg")


