import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from PIL import Image, ImageTk
import os
from MinMaxCompression import maxPixelValue
global minImage, maxImage


imageList = []
imageVariables = []

def openMinMax():

    testImage = imageList[0][0]
    # width, height = testImage.size
    width = testImage.width()
    height = testImage.height()

    max_imgR = [[0] * height for _ in range(width)]
    max_imgG = [[0] * height for _ in range(width)]
    max_imgB = [[0] * height for _ in range(width)]
    
    maxImage = maxPixelValue(imageList, max_imgR, max_imgG, max_imgB)

    # minImage

def openFolder():
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