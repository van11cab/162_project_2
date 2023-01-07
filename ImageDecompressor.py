import pickle
from PIL import Image, ImageOps
import numpy as np
import os
import time

def decompressImages(compressedFile): #this function takes the compressed single file as an argument and extracts every compressed images that it contains
    print("Image Extraction Starting ...")
    start = time.perf_counter()
    
    #line 12-19: intialization of the extractedFolder that would house the transformed/compressed images
    extractedFolder = "./extractedImages/"
    if not os.path.exists(extractedFolder):
        os.mkdir(extractedFolder)

    for fileName in os.listdir(extractedFolder):
        file = extractedFolder + fileName
        if os.path.isfile(file):
            os.remove(file) 

    #line 22-36: initialization and transformation of the compressed file from an list of arrays to its own images and its saved to the newly created extractedFolder
    with open(compressedFile, "rb") as file:
        compressedImage = pickle.load(file)

    for i in range(len(compressedImage)):
        imageWidth = len(compressedImage[0])
        imageHeight = len(compressedImage[0][0])
        blankRGBImage = np.zeros((imageWidth, imageHeight, 3), np.uint8)
        for x in range(imageWidth):
            for y in range(imageHeight):
                blankRGBImage[x][y] = (compressedImage[i][x][y][0], compressedImage[i][x][y][1], compressedImage[i][x][y][2])
        
        extractedImage = Image.fromarray(blankRGBImage)
        extractedImage = ImageOps.mirror(extractedImage)
        extractedImage = extractedImage.rotate(90, expand=1)
        extractedImage.save(f"{extractedFolder}extractedImage-{i}", "JPEG")

    end = time.perf_counter()

    imageExtractionTime = end-start
    
    #line 43-51: calculate for the total size of the compressed images as well as the average file size for each. the value gathered in this process is returned to the main function
    extractedImages = os.listdir(extractedFolder)
    totalSize = 0
    for images in extractedImages:
        totalSize += os.path.getsize(f"{extractedFolder+images}")

    extractedImageTotalSize = totalSize/1024
    extractedImageAverageSize = extractedImageTotalSize/len(extractedImages)

    return extractedFolder, imageExtractionTime, extractedImageTotalSize, extractedImageAverageSize