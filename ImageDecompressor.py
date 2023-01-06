import pickle
from PIL import Image
import numpy as np
import os

def decompressImages(compressedFile):

    extractedFolder = "./extractedImages"
    if not os.path.exists(extractedFolder):
        os.mkdir(extractedFolder)

    with open(compressedFile, "rb") as file:
        compressedImage = pickle.load(file)

    for i in range(len(compressedImage)):
        testArray = compressedImage[i]
        testArray = np.array(testArray)
        testImage = Image.fromarray((testArray*255).astype(np.uint8))

        

        testImage.show()

    # print(compressedImages.read())
    
    # print(compressedImages)


# compressedFile = "./compressedFile.cmp"
# decompressImages(compressedFile)