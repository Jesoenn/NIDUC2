from fileinput import close
from PIL import Image


def get_image_bytes():
    """ Zwraca piksele jako bytearray """
    image_path = "image.png"
    img = Image.open(image_path).convert("RGB")
    img_size = list(img.size)
    pixels = list(img.getdata())  # Pixel list (R, G, B) | LIST -> Tuple

    image_bytes = bytearray()
    for pixel in pixels:
        image_bytes.extend(pixel)

    return image_bytes,img_size


def create_image(image_byte_blocks, image_size):
    image_bytes = bytearray()
    pixels_number = image_size[0]*image_size[1]
    for byte_block in image_byte_blocks:
        image_bytes.extend(byte_block)
    pixels_RGB = []
    pixel = bytearray()
    i = 0
    for byte in image_bytes:
        pixel.append(byte)
        i+=1
        if i == 3:
            pixels_RGB.append(tuple(pixel))
            pixel = bytearray()
            i=0
            if len(pixels_RGB)==pixels_number:
                break

    img = Image.new("RGB", image_size)
    img.putdata(pixels_RGB)
    img.save("image_compiled.png")