from BSC import BSC
from transmitter import Transmitter


#bit error rate - GOOD
transmitter=Transmitter()
byte_32_blocks=transmitter.prepare_to_transmit() # image to send in byte format | list->bytearray

channel_good=BSC("GOOD")
channel_good.receiver(byte_32_blocks)


