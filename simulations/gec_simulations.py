from common.interleaving_mode import InterleavingMode
from common.channel_type import Channel
from common.code_type import CodeType
from common.channel_states import ChannelStates
from communication.transmitter import Transmitter
from communication.satellite import Satellite
from utils import testing
from models.GEC import GEC
from utils.image_operations import visualize_gec, visualize_states


def test_visualization_rs():
    print("test_visualization_rs initialized.")
    transmitter = Transmitter()
    transmitter.get_image()
    transmitter.prepare_to_transmit(InterleavingMode.WITH_INTERLEAVING, 249, 6, CodeType.RS)
    channel = GEC()
    noise_bit_blocks = channel.simulation("GOOD", transmitter.encoded_interlaced_bit_blocks)
    visualize_gec(noise_bit_blocks, transmitter.encoded_interlaced_bit_blocks)
    visualize_states(channel.state_blocks)