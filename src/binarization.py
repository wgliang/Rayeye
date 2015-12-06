from pytesser import *
from PIL import Image
import ImageEnhance
import os

def binariza(path):
    img = Image.open(path) 
    img = img.convert("RGBA")
    pixdata = img.load()

    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][0] < 90:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][1] < 136:
                pixdata[x, y] = (0, 0, 0, 255)
    for y in xrange(img.size[1]):
        for x in xrange(img.size[0]):
            if pixdata[x, y][2] > 0:
                pixdata[x, y] = (255, 255, 255, 255)
    i = path.rfind('/')
    name = path[i+1:]
    img.save('../res/'+ name, "GIF")
    # im_orig = Image.open('input-black.gif')
    # big = im_orig.resize((1000, 500), Image.NEAREST)

if __name__=='__main__':
    path = '../pic/bina/'
    for pic in os.listdir(path):
        if pic.endswith(".gif"):
            print path+pic
            binariza(path+pic)