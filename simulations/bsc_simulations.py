from common.interleaving_mode import InterleavingMode
from common.channel_type import Channel
from common.code_type import CodeType
from common.channel_states import ChannelStates
from communication.transmitter import Transmitter
from communication.satellite import Satellite
from utils import testing
from models.BSC import BSC
from utils import bsc_visualizations
from utils.bsc_visualizations import visualize_errors
from utils.testing import bsc_noise_comparison
from utils.image_operations import create_image
from utils.data_comparison import *


def file_writing_test_interleaving():
    print("file_writing_test_interleaving initialized.")
    transmitter = Transmitter()
    transmitter.get_image()
    satellite = Satellite(transmitter.image_size)
    channel_qualities = [ChannelStates.GOOD, ChannelStates.MEDIUM, ChannelStates.BAD]
    for channel_quality in channel_qualities:
        print("Channel BSC: " + str(channel_quality))
        channel = BSC(channel_quality)
        transmitter.prepare_to_transmit(InterleavingMode.WITH_INTERLEAVING, 249, 6, CodeType.RS)
        noise_bit_blocks = channel.simulation(transmitter.encoded_interlaced_bit_blocks)
        satellite.receive_bit_blocks(noise_bit_blocks, InterleavingMode.WITH_INTERLEAVING, Channel.BSC, CodeType.RS, 6)
        testing.bsc_noise_comparison(CodeType.RS, transmitter.encoded_interlaced_bit_blocks, noise_bit_blocks,channel_quality, channel.bit_error_rate, "bit")
        testing.bsc_noise_comparison(CodeType.RS, transmitter.encoded_interlaced_byte_blocks,satellite.encoded_interlaced_byte_blocks, channel_quality,channel.bit_error_rate,"byte")
        testing.decoder_success_rate(channel_quality,channel.bit_error_rate,len(satellite.decoded_byte_blocks),satellite.count_decoded,satellite.count_failed,len(satellite.decoded_byte_blocks[0]),InterleavingMode.WITH_INTERLEAVING,Channel.BSC,CodeType.RS)
        print(str(channel_quality)+" finished.")


def channel_parameters_test():
    print("channel_parameters_test initialized.")
    transmitter = Transmitter()
    transmitter.get_image()
    #channel_qualities = [ChannelStates.GOOD, ChannelStates.MEDIUM, ChannelStates.BAD]
    channel_qualities = [ChannelStates.GOOD,ChannelStates.GOOD,ChannelStates.MEDIUM,ChannelStates.MEDIUM,ChannelStates.BAD]
    temp=0
    channel_ber= [1/10000,3/10000, 1/1000, 2/1000, 2/100] # G,G,M,M,B
    for channel_quality in channel_qualities:
        channel = BSC(channel_quality)
        channel.bit_error_rate=channel_ber[temp]
        temp+=1
        transmitter.prepare_to_transmit(InterleavingMode.WITHOUT_INTERLEAVING, 249, 6, CodeType.RS)
        for i in range(100):
            print("Quality: " + str(channel_quality)+" | Try: "+str(i+1))
            noise_bit_blocks = channel.simulation(transmitter.encoded_bit_blocks)
            testing.bsc_noise_comparison(CodeType.RS,transmitter.encoded_bit_blocks,noise_bit_blocks,channel_quality,channel.bit_error_rate,"bit")

def channel_parameters_test_images():
    print("channel_parameters_test_images initialized.")
    transmitter = Transmitter()
    transmitter.get_image()
    channel_qualities = [ChannelStates.GOOD, ChannelStates.GOOD, ChannelStates.MEDIUM, ChannelStates.MEDIUM, ChannelStates.BAD]
    channel_ber = [1 / 10000, 3 /10000, 1/1000, 2/1000, 2 / 100]  # G,G,M,M,B
    temp=0
    for channel_quality in channel_qualities:
        channel = BSC(channel_quality)
        print(channel_ber[temp])
        channel.bit_error_rate = channel_ber[temp]
        temp += 1
        transmitter.prepare_to_transmit(InterleavingMode.WITHOUT_INTERLEAVING, 249, 6, CodeType.RS)
        noise_bit_blocks = channel.simulation(transmitter.encoded_bit_blocks)
        visualize_errors(noise_bit_blocks,transmitter.encoded_bit_blocks,channel.bit_error_rate,channel_quality)

def rs_tests():
    print("rs_tests initialized.")
    transmitter = Transmitter()
    transmitter.get_image()
    satellite = Satellite(transmitter.image_size)
    channel_qualities = [ChannelStates.GOOD, ChannelStates.MEDIUM, ChannelStates.BAD]
    #channel_qualities = [ChannelStates.BAD]
    # [1, 3, 10]
    correction = 10
    for channel_quality in channel_qualities:
        channel = BSC(channel_quality)
        for i in range(100):
            print("Quality: " + channel_quality.value + " | Corrections: " + str(correction) + " | Try: " + str(i + 1))
            transmitter.prepare_to_transmit(InterleavingMode.WITHOUT_INTERLEAVING, 255 - correction * 2, correction * 2,CodeType.RS)
            noise_bit_blocks = channel.simulation(transmitter.encoded_bit_blocks)
            satellite.receive_bit_blocks(noise_bit_blocks, InterleavingMode.WITHOUT_INTERLEAVING, Channel.BSC,CodeType.RS, correction * 2)

            count_decoded_blocks, count_failed_blocks, decoded_symbols, not_decoded_symbols=compare_bytes(satellite.decoded_byte_blocks,transmitter.original_byte_blocks)
            testing.decoder_success_rate(channel_quality, channel.bit_error_rate, len(satellite.decoded_byte_blocks),decoded_symbols,
                                         not_decoded_symbols,len(satellite.decoded_byte_blocks[0]), InterleavingMode.WITHOUT_INTERLEAVING,
                                         Channel.BSC, CodeType.RS,"Bytes")
            testing.decoder_success_rate(channel_quality, channel.bit_error_rate, len(satellite.decoded_byte_blocks),count_decoded_blocks,
                                         count_failed_blocks,len(satellite.decoded_byte_blocks[0]), InterleavingMode.WITHOUT_INTERLEAVING,
                                         Channel.BSC, CodeType.RS,"Blocks")


            testing.bsc_noise_comparison(CodeType.RS, transmitter.encoded_byte_blocks, satellite.encoded_byte_blocks,channel_quality, channel.bit_error_rate, "byte")
def rs_tests_visualization():
    print("rs_tests initialized.")
    transmitter = Transmitter()
    transmitter.get_image()
    satellite = Satellite(transmitter.image_size)
    channel_qualities = [ChannelStates.GOOD, ChannelStates.MEDIUM, ChannelStates.BAD]
    corrections = [1, 3, 10]
    for channel_quality in channel_qualities:
        channel = BSC(channel_quality)
        for correction in corrections:
            print("Quality: "+channel_quality.value+" | Corrections: "+str(correction))
            transmitter.prepare_to_transmit(InterleavingMode.WITHOUT_INTERLEAVING, 255-correction*2, correction*2, CodeType.RS)
            noise_bit_blocks = channel.simulation(transmitter.encoded_bit_blocks)
            satellite.receive_bit_blocks(noise_bit_blocks, InterleavingMode.WITHOUT_INTERLEAVING, Channel.BSC, CodeType.RS, correction*2)
            create_image(satellite.decoded_byte_blocks,satellite.image_size,Channel.BSC.value,channel_quality.value, correction*2)