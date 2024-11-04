from fileinput import close
from PIL import Image

def get_image_bytes():
    """Returns all bytes from image"""
    image_path="image.png"
    img=open(image_path, "rb")
    return bytearray(img.read())

def create_image(image_byte_blocks):
    """Creates an image from given bytes"""
    image_path="image_compiled.png"
    img=open(image_path, "wb")
    image_bytes=bytearray()
    for byte_block in image_byte_blocks:
        image_bytes.extend(byte_block)
    img.write(image_bytes)
    img.close()


    # image_bytes=bytearray(img.read())
    # print(image_bytes[100])
    # image_bytes[100]=100
