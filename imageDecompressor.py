import pickle
from PIL import Image
import numpy as np

import pickle

def decompressImages(compressedFile):
    # print(compressedFile[0][0]b)
    # print("...")
pickle.load()fielle    with open(compressedFile, "r") as file:
    #     compressedImage = pic
    print(len(compressedImage))

    for i in range(len(compressedImage)):

        testArray = compressedImage[i]
        testArray = np.array(testArray)
        testImage = Image.fromarray((testArray*255).astype(np.uint8))
        testImage.show()kle.load(compressedFile)
        # compressedImages = file
    print(compressedImage[0])

    # print(compressedImages.read())
    
    # print(compressedImages)
# 
# # def stringtoarray(compressedFile):
#     for letter in range(len(compressedFile)):
#         if letter == "[":
            #if open brackets, create an empty array
            



compressedFile = "./compressedFile.cmp"
decompressImages(compressedFile)