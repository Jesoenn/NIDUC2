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


def create_image(image_byte_blocks, image_size):
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
    img.save("image_compiled.png")