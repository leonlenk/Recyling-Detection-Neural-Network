# pip install pillow
from PIL import Image, ImageOps
import os
import numpy as np

path = "C:/Users/leonl/Documents/ProgramingProjects/CanProjects"
dirs = [path+"/can/"]
outputdir = path+"/OutputCans/"   # this directory must exist!
imageSize = 64

def correctimage(filepath, pixelsize):
    image = Image.open(filepath)
    image = image.resize((pixelsize, pixelsize))
    image = ImageOps.grayscale(image)
    image = ImageOps.exif_transpose(image)
    return image

# the following saves output images and save a NumPy array A that is in the form that Keras wants
for dir in dirs:
    A = np.empty((0,imageSize,imageSize), np.float32)    
    number = 1
    for filename in os.listdir(dir):
        if filename.endswith(".jpg" or "JPG"):
            print(dir+filename)
            outtag = "can"
            image = correctimage(dir+filename, imageSize)
            image.save(outputdir + "Output"+outtag+str(number)+ ".jpeg")
            #image.show()
            number = number + 1

            im = np.array(image, np.float32) / 255.0        # from Pillow to NumPy
            row = im.reshape((1,imageSize,imageSize))
            rowFlippedHorizontally = np.flip(im, 1).reshape((1,imageSize,imageSize))
            #A = np.vstack([A, row])
            A = np.vstack([A, row, rowFlippedHorizontally, np.flip(row), np.flip(rowFlippedHorizontally)])
            number = number + 1 
    np.save(outtag+'Data.npy', A)