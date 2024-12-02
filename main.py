
from BSC import BSC
from transmitter import Transmitter
from satellite import Satellite
from GEC import GEC 
import testing


transmitter = Transmitter()
transmitter.get_image()
satellite = Satellite(transmitter.image_size)

channel_used = "BSC"
transmission_types= ["interlace","normal"]
channels = ["GOOD","MEDIUM","BAD"]
for chosen_channel in channels:
    channel = BSC(chosen_channel)
    transmission_type="interlace"
    #for transmission_type in transmission_types:
    for i in range(1):
        transmitter.prepare_to_transmit(transmission_type)  # interlace, normal
        if transmission_type == "interlace":
            noise_bit_blocks = channel.simulation(transmitter.encoded_interlaced_bit_blocks)
        else:
            noise_bit_blocks = channel.simulation(transmitter.encoded_bit_blocks)
        satellite.receive_bit_blocks(noise_bit_blocks, transmission_type, channel_used)

        # testy
        testing.decoder_success_rate(chosen_channel, channel.bit_error_rate, len(satellite.decoded_byte_blocks),
                                     satellite.count_decoded, satellite.count_failed)
        testing.noise_comparison(transmitter.encoded_interlaced_bit_blocks, noise_bit_blocks,
                                 transmitter.encoded_byte_blocks, satellite.encoded_byte_blocks, chosen_channel,
                                 channel.bit_error_rate)
"""
states =["GOOD","BAD"]
for chosen_state in states:
    gec = GEC()
    for i in range(2):
        # Simulacja przesylu bitow
        noise_bit_255_interlaced_blocks = gec.simulation(chosen_state,transmitter.encoded_interlaced_bit_blocks)
        satellite.receive_bit_blocks(noise_bit_255_interlaced_blocks)  # Odbiot blokow bitow
        satellite.encoded_byte_blocks = satellite.bits_to_bytes(satellite.encoded_bit_blocks)  # zamiana bitow na bajty
        satellite.encoded_byte_blocks = satellite.deinterlace(satellite.encoded_byte_blocks)  # Odwrocenie przeplotu
        count_decoded, count_failed = satellite.decode("gec")  # policzenie ile dekodowan sie powiodlo, a ile nie
        testing.decoder_success_rate_in_GEC_channel(chosen_state, gec.k,gec.b_no_err_to_good, gec.h, len(satellite.decoded_byte_blocks),
                                     count_decoded, count_failed)
        testing.noise_comparison_in_GEC_channel(transmitter.encoded_interlaced_bit_blocks, noise_bit_255_interlaced_blocks,
                                 transmitter.encoded_byte_blocks, satellite.encoded_byte_blocks, chosen_state,
                                                gec.k, gec.b_no_err_to_good, gec.h)
"""

