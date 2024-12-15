import math
from turtledemo.sorting_animate import start_ssort

from PIL import Image



def get_image_bytes():
    """
    Pobranie zdjecia (wylacznie jego pikseli)
    Parametry:
        - pixels: list -> tuple
        - img_size: list -> int
        - image_bytes: bytearray
    Zwraca:
        - image_bytes,img_size
    """
    image_path = "image.png"
    img = Image.open(image_path).convert("RGB")
    img_size = list(img.size)
    pixels = list(img.getdata())  # Pixel list (R, G, B)

    image_bytes = bytearray()
    for pixel in pixels:
        image_bytes.extend(pixel)

    return image_bytes,img_size


def create_image(image_byte_blocks, image_size, channel_used):
    """
    Na podstawie otrzymanych blokow pixeli, tworzy zdjecie o okreslonym rozmiarze
    Parametry:
        - image_byte_blocks: list->bytearray
        - image_size: list->int
        - image_bytes: bytearray
        - pixels_RGB: list->tuple->bytearray (w kazdym tuple po 3 pixele - RGB)
        - pixel: bytearray (o dlugosci 3 - RGB)
    """
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
    imgName ="image_compiled_"+str(channel_used)+".png"
    img.save(imgName)

def visualize_gec(noise_bit_blocks, original_bit_blocks):
    #rect = int(math.sqrt(len(noise_bit_blocks)*len(noise_bit_blocks[0])))
    #image_size=tuple([rect,rect])
    height = len(noise_bit_blocks)  # Liczba wierszy
    width = len(noise_bit_blocks[0])
    image_size = (width, height)
    pixels=[]
    for i in range (height):
        for j in range(width):
            if noise_bit_blocks[i][j] != original_bit_blocks[i][j]:
                pixels.append(tuple([0,0,0]))
            else:
                pixels.append(tuple([255,255,255]))

    img = Image.new("RGB", image_size)
    img.putdata(pixels)
    imgName = "GEC_Visualization.png"
    img.save(imgName)
    print("IMAGE CREATED")


def visualize_states(state_list):
    height = len(state_list)  # Liczba wierszy
    width = len(state_list[0])
    image_size = (width, height)
    pixels = []
    for i in range(height):
        for j in range(width):
            if state_list[i][j] == "1":
                pixels.append(tuple([0,0,0]))
            else:
                pixels.append(tuple([217, 67, 90]))

    img = Image.new("RGB", image_size)
    img.putdata(pixels)
    imgName = "STATE_LIST_Visualization.png"
    img.save(imgName)
    print("STATES IMAGE CREATED")
