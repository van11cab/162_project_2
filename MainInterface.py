import pickle
import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk, ImageOps
import os
from CalculateLevels import calculatePixelLevels
from MinMaxCompression import maxPixelValue, minPixelValue
from ImageDecompressor import decompressImages

imageList = []
imageVariables = []

def openMinMax():
    
    global minImage, maxImage
    maxImage = maxPixelValue(folderPath)
    # maxImage.show()
    maxImage = ImageOps.mirror(maxImage)
    # maxImage.show()
    maxImage = maxImage.rotate(90, expand = 1)
    # maxImage.show()


    minImage = minPixelValue(folderPath)
    # minImage.show()
    minImage = ImageOps.mirror(minImage)
    # minImage.show()
    minImage = minImage.rotate(90, expand=1)
    # minImage.show()
    
    compresssed_img_lib = calculatePixelLevels(folderPath, minImage, maxImage)
    print("done compressing")


    #assume uncompressed form is exactly the same as the compressed_img_lib
    decompressed_img_lib = decoder(compresssed_img_lib)
    
    with open("compressedFile.cmp", "wb") as compressedImage:
        pickle.dump(compresssed_img_lib, compressedImage)

    # print(compresssed_img_lib)
    print("displaying images ...")
    decompressImages("compressedFile.cmp")


    # maxImage.show()
    # minImage.show()

def decoder(compresssed_img_lib):
    #get the max and min of each image
    
    return 0


def openCalculateLevels():
    print("...")

# def openImageDecompression():
#     compressedFile = "./compressedFile.cmp"
#     decompressImages(compressedFile)
#     print("...")


def openFolder():
    global folderPath
    folderPath = filedialog.askdirectory()
    imageFiles = os.listdir(folderPath)

    for i in range(0, len(imageFiles)):
        imageList.append([
            ImageTk.PhotoImage(Image.open(folderPath+'/'+imageFiles[i]).resize((50,50))),
            ImageTk.PhotoImage(Image.open(folderPath+'/'+imageFiles[i])),
        ]),
        imageVariables.append(f"img_{i}")

    for i in range(len(imageVariables)):
        globals()[imageVariables[i]] = tk.Button(imageSlider, image=imageList[i][0], bd=0, command=lambda i=i:displayImage(i))
        globals()[imageVariables[i]].pack(side=tk.LEFT)

    # print("Opening folder ...")

def displayImage(index):
    displayImageLabel.config(image=imageList[index][1])


mainWindow = tk.Tk()
mainWindow.title("CMSC 162 - Final Project")

width = mainWindow.winfo_screenwidth()
height = mainWindow.winfo_screenheight()
mainWindow.geometry("%dx%d" % (width, height))

mainMenuBar = tk.Menu(mainWindow)
mainWindow.config(menu = mainMenuBar)

fileMenu = tk.Menu(mainMenuBar, tearoff=0)
fileMenu.add_command(label="Open Folder", command=openFolder)
mainMenuBar.add_cascade(label="File", menu=fileMenu)

compressionMenu = tk.Menu(mainMenuBar, tearoff=0)
compressionMenu.add_command(label="Min and Max", command=openMinMax)
compressionMenu.add_command(label="Calculate Levels", command=openCalculateLevels)
mainMenuBar.add_cascade(label="Compression", menu=compressionMenu)

displayImageLabel = tk.Label(mainWindow)
displayImageLabel.pack(anchor=tk.CENTER)

thumbnailCanvas = tk.Canvas(mainWindow, height=60)
thumbnailCanvas.pack(side=tk.BOTTOM, fill=tk.X)

xScrollBar = ttk.Scrollbar(mainWindow, orient=tk.HORIZONTAL)
xScrollBar.pack(side=tk.BOTTOM, fill=tk.X)
xScrollBar.config(command=thumbnailCanvas.xview)

thumbnailCanvas.config(xscrollcommand=xScrollBar.set)
thumbnailCanvas.bind("<Configure>", lambda e: thumbnailCanvas.bbox("all"))

imageSlider = tk.Frame(thumbnailCanvas)
thumbnailCanvas.create_window((0,0), window=imageSlider, anchor=tk.NW)

mainWindow.mainloop()