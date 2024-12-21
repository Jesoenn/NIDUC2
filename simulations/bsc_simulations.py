from common.interleaving_mode import InterleavingMode
from common.channel_type import Channel
from common.code_type import CodeType
from common.channel_states import ChannelStates
from communication.transmitter import Transmitter
from communication.satellite import Satellite
from utils import testing
from models.BSC import BSC

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