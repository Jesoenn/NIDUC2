from BSC import BSC
from transmitter import Transmitter
from rs_coder import RS


transmitter=Transmitter()
byte_32_blocks=transmitter.prepare_to_transmit() # image to send in byte format | list->bytearray

# encoding
rs=RS(3)
byte_32_blocks_encoded=rs.encode(byte_32_blocks[:])
# interlacing encoded blocks
byte_32_interlaced_blocks=transmitter.interlace(byte_32_blocks_encoded[:])

# simulating bits traveling through channel
channel_good=BSC("GOOD")
channel_good.receiver(byte_32_blocks)


