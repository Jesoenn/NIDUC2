from BSC import BSC
from transmitter import Transmitter


#bit error rate - GOOD
transmitter=Transmitter()
byte_32_blocks=transmitter.prepare_to_transmit() # image to send in byte format | list->bytearray
byte_32_interlaced_blocks=transmitter.interlace(byte_32_blocks)

# sprawdzenie przeplotu mniej wiecej
print(byte_32_blocks[0][0],byte_32_blocks[1][0],byte_32_blocks[2][0])
print(byte_32_interlaced_blocks[0][0],byte_32_interlaced_blocks[0][1],byte_32_interlaced_blocks[0][2])


channel_good=BSC("GOOD")
channel_good.receiver(byte_32_blocks)


