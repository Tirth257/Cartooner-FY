from PIL import Image
import numpy as np
from math import *
import matplotlib.pyplot as plt
from tkinter import Tk
from tkinter.filedialog import askopenfilename
import sys

getMagRGB = lambda r,g,b: sqrt(r**2 + g**2+ b**2)

def getDis(p1,p2):
    C1 = img_data[p1]
    C2 = img_data[p2]
    return getMagRGB(C1[0]-C2[0],C1[1]-C2[1],C1[2]-C2[2])
def getDisWithavg(p1,avg_col):
    C1 = img_data[p1]
    return getMagRGB(C1[0]-avg_col[0],C1[1]-avg_col[1],C1[2]-avg_col[2])

separator = lambda:print("-"*60)
def FlagR(loc,Thres):
    global avg,seg_points_reg,img_data,lonelyTargets,registery
    allowables = 4
    y = loc[0]
    while y < HEIGHT:
        x = loc[1]
        flag = 0
        while x < WIDTH:
            
            if registery[(y,x)] == 0:
                if Thres > getDisWithavg((y,x),avg):
                    avg = (avg*len(seg_points_reg) + img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1
                else:
                    flag += 1
                    if flag > allowables:
                        lonelyTargets.add((y,x))
                        break
            x+=1
        x = loc[1]
        flag = 0
        while x >= 0:
            if registery[(y,x)] == 0 :
                if Thres > getDisWithavg((y,x),avg):

                    avg = (avg*len(seg_points_reg) + img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1
                else:
                    flag += 1
                    if flag > allowables:
                        lonelyTargets.add((y,x))
                        break

            x-=1
        y+=1
        
    y = loc[0]

    while y >=0:
        x = loc[1]
        flag = 0
        while x < WIDTH:
            if registery[(y,x)] == 0:
                if Thres > getDisWithavg((y,x),avg):

                    avg = (avg*len(seg_points_reg) +img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1
                else:
                    flag += 1
                    if flag >allowables:
                        lonelyTargets.add((y,x))
                        break


            x+=1
        x = loc[1]
        flag = 0
        while x >= 0:

            if registery[(y,x)] == 0:
                
                if Thres > getDisWithavg((y,x),avg):
                    
                    avg = (avg*len(seg_points_reg) + img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1
                else:
                    flag += 1
                    if flag >allowables:
                        lonelyTargets.add((y,x))
                        break

            x-=1
        y-=1

def RforNeighbour(loc,Thres):
    global avg,seg_points_reg,img_data,lonelyTargets,registery

    y = loc[0]
    while y < HEIGHT:
        x = loc[1]
        while x < WIDTH:
            if registery[(y,x)] == 0:
                if Thres > getDisWithavg((y,x),avg):
                    avg = (avg*len(seg_points_reg) + img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1


                else:
                    lonelyTargets.add((y,x))

            x+=1
        x = loc[1]
        while x >= 0:
            if registery[(y,x)] == 0 :
                if Thres > getDisWithavg((y,x),avg):

                    avg = (avg*len(seg_points_reg) + img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1


                else:
                    lonelyTargets.add((y,x))


            x-=1
        y+=1
    y = loc[0]

    while y >=0:
        x = loc[1]
        while x < WIDTH:
            if registery[(y,x)] == 0:
                if Thres > getDisWithavg((y,x),avg):

                    avg = (avg*len(seg_points_reg) +img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1

                else:
                    lonelyTargets.add((y,x))


            x+=1
        x = loc[1]
        while x >= 0:

            if registery[(y,x)] == 0:
                
                if Thres > getDisWithavg((y,x),avg):
                    
                    avg = (avg*len(seg_points_reg) + img_data[(y,x)])/(len(seg_points_reg)+1)
                    seg_points_reg.add((y,x))
                    lonelyTargets.discard((y,x))
                    registery[(y,x)] = 1


                else:
                    lonelyTargets.add((y,x))

            x-=1
        y-=1

def Run(Thres,algo):
    global avg,seg_points_reg,lonelyTargets,img_data,registery
    while len(lonelyTargets) != 0:

        loc = next(iter(lonelyTargets))
        avg = img_data[loc]
        registery[loc] = 1
        seg_points_reg = {loc}
        lonelyTargets.discard(loc)
        if algo == "1":
            RforNeighbour(loc,Thres)
        else:
            FlagR(loc,Thres)

        for e in seg_points_reg:
            img_data[e] = avg

def AskFile():

    print("Choose an image")
    while True:
        path = askopenfilename()

        try:
            im = Image.open(path)
            im.verify()  
            print("Image loaded successfully:")
            im = Image.open(path).convert("RGB")
            return im
        except Exception as e:
            print("Failed to load image")
            q = input("If you want to quit, press q")
            if q == "q":
                sys.exit()


    
def AskThres():
    thres = 40
    separator()
    print("More ThresHold means Less Colour variety (Optimal value is around 40)")
    print("(enter nothing to choose default value)")
    try:

        thres = int(input("Threshold :- "))
        
    except:
        thres = 40 
    return thres
def chooseAlgo():
    separator()
    print("Choose Algorithm")
    print("1. Global Sampling-","(Best in most of the cases)")
    print("2. Local Sampling")

    inp = input("Choose :- ")
    if inp == "2":
        return "2"
    else:
        return "1"
def AfterMath():
    separator()
    print("image created successfully")
    separator()
    print("Choose The following Actions")
    print("1. Retry With a different Threshold and Algorithm")
    print("2. Choose new image")
    print("3. exit")
    an = input("Choose Action :- ")
    return an
while True:
    
    root = Tk()
    root.withdraw()
    im = AskFile()
    root.destroy()
    while True:
        Thres = AskThres()

        algo = chooseAlgo()
        
        print("It may take around 10-15 seconds")
        img_data = np.array(im)
        
        registery = np.zeros((img_data.shape[0],img_data.shape[1]))
        HEIGHT = img_data.shape[0]
        WIDTH = img_data.shape[1];
        rows, cols = np.indices((HEIGHT, WIDTH))
        
        
        lonelyTargets = {(2,2)};
        avg = np.zeros(3)
        seg_points_reg = {}
        img_data = img_data.astype(float);
        
        Run(Thres,algo)
        img_data = img_data.astype(np.uint8)
        pil_image = Image.fromarray(img_data)

        plt.figure()
        plt.imshow(pil_image)
        plt.axis('off')
        plt.title("Image")
        plt.show(block=False)

        action = AfterMath()
        if action == "1":
            continue
        elif action == "2":
            break
        else:
            sys.exit()