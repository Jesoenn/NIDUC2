import math
import os
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
    image_path = "./resources/image.png"
    img = Image.open(image_path).convert("RGB")
    img_size = list(img.size)
    pixels = list(img.getdata())  # Pixel list (R, G, B)

    image_bytes = bytearray()
    for pixel in pixels:
        image_bytes.extend(pixel)

    return image_bytes,img_size


def create_image(image_byte_blocks, image_size, channel_used: str, channel_quality: str,parity_size: int):
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

    if channel_used=="BSC":
        output_file_path = os.path.join(os.getcwd(), "output/images/bsc_images/img_compiled_"+channel_quality+"_"+str(parity_size)+".png")
    else:
        output_file_path = os.path.join(os.getcwd(), "output/images/gec_images/img_compiled_"+channel_quality+"_"+str(parity_size)+".png")
    img.save(output_file_path)

def visualize_gec(noise_bit_blocks, original_bit_blocks):
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
    output_file_path = os.path.join(os.getcwd(), "output/images/gec_images/GEC_Visualization.png")
    img.save(output_file_path)
    print("GEC Visualization created")


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
    output_file_path = os.path.join(os.getcwd(), "output/images/gec_images/STATE_LIST_Visualization.png")
    img.save(output_file_path)
    print("States Visualization created")
