import os
from PIL import Image
from common.channel_states import ChannelStates

def visualize_errors(noise_bit_blocks, original_bit_blocks, bit_error_rate: float, channel_quality: ChannelStates):
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

    bit_error_rate = f"{bit_error_rate:.0e}".replace('e', ' 10^')

    output_file_path = os.path.join(os.getcwd(), "output/images/bsc_images/BER_tests/BSC_"+channel_quality.value+"_"+bit_error_rate+".png")
    img.save(output_file_path)
    print("BSC Visualization created")