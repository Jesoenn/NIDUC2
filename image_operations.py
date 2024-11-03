from fileinput import close

from PIL import Image


def getImageBytes():
    image_path="image.png"
    img=open(image_path, "rb")
    return bytearray(img.read())

def createImage(image_bytes):
    image_path="image_compiled.png"
    img=open(image_path, "wb")
    img.write(image_bytes)


    # image_bytes=bytearray(img.read())
    # print(image_bytes[100])
    # image_bytes[100]=100