from common.channel_states import ChannelStates
from common.code_type import CodeType
from common.interleaving_mode import InterleavingMode
from models.BSC import BSC
from simulations.bsc_simulations import *
from simulations.gec_simulations import test_visualization_rs
from utils.image_operations import visualize_gec, visualize_states
from communication.transmitter import Transmitter
from communication.satellite import Satellite
from models.GEC import GEC
from simulations import bsc_simulations
from common import channel_states, code_type, interleaving_mode
from utils import testing

#channel_parameters_test()
#channel_parameters_test_images()

rs_tests()

"""
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

        # testy (TYLKO DLA PRZEPLOTU)
        testing.decoder_success_rate(chosen_channel, channel.bit_error_rate, len(satellite.decoded_byte_blocks),
                                     satellite.count_decoded, satellite.count_failed)
        testing.noise_comparison(transmitter.encoded_interlaced_bit_blocks, noise_bit_blocks,
                                 transmitter.encoded_byte_blocks, satellite.encoded_byte_blocks, chosen_channel,
                                 channel.bit_error_rate)
                                 
states =["GOOD","BAD"]
for chosen_state in states:
    gec = GEC()
    for transmission_type in transmission_types:
        for i in range(1):
            transmitter.prepare_to_transmit(transmission_type)

            if transmission_type == "interlace":
                noise_bit_blocks = gec.simulation(chosen_state,transmitter.encoded_interlaced_bit_blocks)
                satellite.receive_bit_blocks(noise_bit_blocks, transmission_type, "gecInterlace")
            else:
                noise_bit_blocks = gec.simulation(chosen_state,transmitter.encoded_bit_blocks)
                satellite.receive_bit_blocks(noise_bit_blocks, transmission_type, "gecNoInteralce")

            if transmission_type == "interlace":
                testing.decoder_success_rate_in_GEC_channel(chosen_state, gec.k, gec.p_to_good, gec.p_to_bad, gec.h,
                                                            len(satellite.decoded_byte_blocks),
                                                            satellite.count_decoded, satellite.count_failed, "true")
                testing.noise_comparison_in_GEC_channel(transmitter.encoded_interlaced_bit_blocks,
                                                        noise_bit_blocks,
                                                        transmitter.encoded_byte_blocks, satellite.encoded_byte_blocks,
                                                        chosen_state,
                                                        gec.k, gec.p_to_good,gec.p_to_bad, gec.h, "true")
                # test na występowanie przekłamanych bajtów obok siebie, w celu porównania działania przeplotu
                testing.bits_group_errors_comparison( satellite.encoded_byte_blocks,transmitter.encoded_byte_blocks,"true")
            else:
                testing.decoder_success_rate_in_GEC_channel(chosen_state, gec.k, gec.p_to_good, gec.p_to_bad, gec.h,
                                                            len(satellite.decoded_byte_blocks),
                                                            satellite.count_decoded, satellite.count_failed, "false")
                testing.noise_comparison_in_GEC_channel(transmitter.encoded_bit_blocks,
                                                        noise_bit_blocks,
                                                        transmitter.encoded_byte_blocks, satellite.encoded_byte_blocks,
                                                        chosen_state,
                                                        gec.k, gec.p_to_good, gec.p_to_bad, gec.h, "false")
                # test na występowanie przekłamanych bajtów obok siebie, w celu porównania działania przeplotu
                testing.bits_group_errors_comparison(satellite.encoded_byte_blocks,transmitter.encoded_byte_blocks,
                                                     "false")

"""