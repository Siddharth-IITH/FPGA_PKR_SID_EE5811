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

    # Port Initilization 
    # For sending data to arduino
    port1 = '/dev/ttyACM1' 
    speed1 = 9600
    # For receiving data from arduino
    port2 = '/dev/ttyACM0'
    speed2 = 9600

    ardData1 = serial.Serial(port1,speed1)
    ardData2 = serial.Serial(port2,speed2)
                 
    # Convert PIL Image to NumPy array
    from PIL import Image
    image = Image.open("tiger.bmp")
    img = image.resize((210,118))
    arr = numpy.array(img)
    img = PIL.Image.fromarray(arr)
    
    # Send Array to Arduino
    for i in range(arr.shape[2]):
        im = arr[:,:,i]
        for j in range(im.shape[0]):
            for k in range(im.shape[1]):
                string=str(int(im[j][k]))+'\n'
                # Sending array to arduino
                ardData1.write(string.encode())
                # Receiving array from arduino
                ms = ardData2.readline()
                try:
                    msg=str(ms.decode("utf-8"))
                except:    
                    msg=0
                try:    
                    zz = int(msg)
                except:    
                    zz = 0
                print(im[j][k],zz,j,k )
                im[j][k] = zz
        arr[:,:,i] = im[:,:]    
    print("Colour Inversion is Completed")
    
    # Convert Array to Image and save
    plt.imshow(arr)
    plt.savefig("inverted_tiger.jpg")
    fig = plt.figure(figsize=(8, 8))
    fig.add_subplot(1,2,1)
    plt.imshow(img)
    fig.add_subplot(1,2,2)
    plt.imshow(arr)
    plt.show()
    fig.savefig("both")
