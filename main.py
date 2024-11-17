from BSC import BSC
from transmitter import Transmitter
from satellite import Satellite
import testing

# Transmisja
transmitter=Transmitter() # obiekt transmitera
transmitter.prepare_to_transmit() #  Caly plik podzielony na 249 bajtowe bloki (6 zostawione na 3 bledy korekcyjne)
satellite=Satellite(transmitter.image_size) # obiekt Satelity z okreslonym rozmiarem zdjecia
transmitter.encode() # enkodowanie Reeda Salomona
transmitter.encoded_interlaced_byte_blocks=transmitter.interlace(transmitter.encoded_byte_blocks[:]) # zrobienie przeplotu z zakodowanego ciagu 255 bajtow
transmitter.encoded_interlaced_bit_blocks=transmitter.bytes_to_bits(transmitter.encoded_interlaced_byte_blocks) # zamiana bajtow na bity / przygotowanie do przeslania

# Simulacja przesylu bitow
channel_good=BSC("BAD") # kanal BSC
noise_bit_255_interlaced_blocks=channel_good.simulation(transmitter.encoded_interlaced_bit_blocks) # Odbior bitow i symulacja szumu

# Odbior satelity
satellite.receive_bit_blocks(noise_bit_255_interlaced_blocks) # Odbiot blokow bitow
satellite.encoded_byte_blocks=satellite.bits_to_bytes(satellite.encoded_bit_blocks) # zamiana bitow na bajty
satellite.encoded_byte_blocks=satellite.deinterlace(satellite.encoded_byte_blocks) # Odwrocenie przeplotu
count_decoded,count_failed=satellite.decode() # policzenie ile dekodowan sie powiodlo, a ile nie


testing.decoder_success_rate("BAD", channel_good.bit_error_rate, len(satellite.decoded_byte_blocks),count_decoded,count_failed)
testing.noise_comparison(transmitter.encoded_interlaced_bit_blocks,noise_bit_255_interlaced_blocks,"BAD",channel_good.bit_error_rate)