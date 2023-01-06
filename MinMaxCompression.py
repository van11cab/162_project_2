import os
import numpy as np
from PIL import Image, ImageTk

def maxPixelValue(imageList, maxImgR, maxImgG, maxImgB):

    testImage = imageList[0][1]
    # width, height = testImage.size
    width = testImage.width()
    height = testImage.height()

    for imagetk in imageList:
        print(imagetk)
        image = ImageTk.getimage(imagetk[1])
        for y in range(len(maxImgR[0])):
            for x in range(len(maxImgR)):
                currpixel = image.getpixel((x,y))

                #R
                if(currpixel[0] > maxImgR[x][y]):
                    maxImgR[x][y] = currpixel[0]
                #G
                if(currpixel[1] > maxImgG[x][y]):
                    maxImgG[x][y] = currpixel[1]
                #B
                if(currpixel[2] > maxImgB[x][y]):
                    maxImgB[x][y] = currpixel[2]
                    
    max_img = np.zeros((width, height, 3), dtype = np.uint8)

    for y in range(len(maxImgR[0])):
        for x in range(len(maxImgR)):
            holder= [maxImgR[x][y], maxImgG[x][y], maxImgB[x][y]]
            max_img[x,y] = holder
    final_max = Image.fromarray(max_img)
    final_max.show()
    return final_max

def minPixelValue(path, minImage):
    print("...")
