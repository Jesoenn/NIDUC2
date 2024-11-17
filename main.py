from BSC import BSC
from transmitter import Transmitter
from satellite import Satellite
import testing

# Tworzymy potrzebne obiekty
transmitter=Transmitter()
satellite=Satellite()
# Caly plik podzielony na 249 bajtowe bloki (+6 na 3 bledy korekcyjne)
transmitter.prepare_to_transmit() # image to send in byte format | list->bytearray
transmitter.encode()
transmitter.encoded_interlaced_byte_blocks=transmitter.interlace(transmitter.encoded_byte_blocks[:])
transmitter.encoded_interlaced_bit_blocks=transmitter.bytes_to_bits(transmitter.encoded_interlaced_byte_blocks)

# simulating bits traveling through channel
channel_good=BSC("GOOD")
# Odbior bitow i symulacja szumu
noise_bit_255_interlaced_blocks=channel_good.simulation(transmitter.encoded_interlaced_bit_blocks)

satellite.receive_bit_blocks(noise_bit_255_interlaced_blocks)
satellite.encoded_byte_blocks=satellite.bits_to_bytes(satellite.encoded_bit_blocks)
satellite.encoded_byte_blocks=satellite.deinterlace(satellite.encoded_byte_blocks)
count_decoded,count_failed=satellite.decode()


testing.decoder_success_rate("GOOD", channel_good.bit_error_rate, len(satellite.decoded_byte_blocks),count_decoded,count_failed)
testing.noise_comparison(transmitter.encoded_interlaced_bit_blocks,noise_bit_255_interlaced_blocks,"GOOD",channel_good.bit_error_rate)