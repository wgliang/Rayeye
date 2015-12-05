from pytesser import *
from PIL import Image
import ImageEnhance
import os

def open_picture(path):
    image = Image.open(path)
    try:
        
        enhancer = ImageEnhance.Contrast(image)
        image = enhancer.enhance(4)
        vcode = image_to_string(image)
        vcode = vcode.replace('_','')
        vcode = vcode[:4]
        image.save('res/'+str(vcode)+'.gif','GIF')
        print vcode
    except:
        print path + ' error'


if __name__=='__main__':

    walk_picture('/home/wgliang/Rayeye/pic')