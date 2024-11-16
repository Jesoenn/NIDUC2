from BSC import BSC
from transmitter import Transmitter
from rs_coder import RS
import testing

# Tworzymy transmiter
transmitter=Transmitter()
# Caly plik podzielony na 249 bajtowe bloki (+6 na 3 bledy korekcyjne)
byte_249_blocks=transmitter.prepare_to_transmit() # image to send in byte format | list->bytearray

# enkoder
rs=RS(3)
byte_255_blocks_encoded=rs.encode(byte_249_blocks[:])

# przeplot blokow
byte_255_interlaced_blocks=transmitter.interlace(byte_255_blocks_encoded[:])

# zamiana blokow na bity
bit_255_blocks_encoded=transmitter.bytes_to_bits(byte_255_blocks_encoded)
bit_255_interlaced_blocks=transmitter.bytes_to_bits(byte_255_interlaced_blocks)

# simulating bits traveling through channel
channel_good=BSC("GOOD")

# Odbior bitow i symulacja szumu
noise_bit_255_interlaced_blocks=channel_good.simulation(bit_255_interlaced_blocks)
testing.compare_bit_blocks(bit_255_interlaced_blocks,noise_bit_255_interlaced_blocks)


