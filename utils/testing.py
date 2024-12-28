from common.channel_states import ChannelStates
from common.channel_type import Channel
from common.code_type import CodeType
from common.interleaving_mode import InterleavingMode
from utils import file_operations
from common import interleaving_mode,code_type, channel_states, channel_type

def compare_blocks(original_block, noise_block):
    """Porownanie kazdego kazdego bitu do siebie
    Parametry:
        - original_block, noise_block: list->bytearray/string
        - block_changes: list->int
    Zwraca:
        - block_changes
    """
    block_changes = list()
    for i in range(len(original_block)):
        changes = 0
        for j in range(len(original_block[0])):
            if original_block[i][j] != noise_block[i][j]:
                changes += 1
        block_changes.append(changes)
    return block_changes

def bsc_noise_comparison(code: CodeType, blocks, noise_blocks,channel: ChannelStates, ber, unit_type: str):
    """Uniwersalnie porownuje dwa sygnaly i wpisuje do plikow wyniki
    Parametry:
        - unit_type: "bit" albo "byte"
        - blocks, noise_blocks: list->string lub bytearray"""

    errors_list=compare_blocks(blocks, noise_blocks)
    total_errors=sum(errors_list)
    file_operations.write_bsc_noise_comparison(channel.value, ber, len(blocks) * len(blocks[0]), total_errors, len(blocks), total_errors / len(blocks), unit_type, code.value)

def decoder_success_rate(channel_quality: ChannelStates, ber: float, total_blocks: int,count_decoded: int,count_failed: int,block_size: int,
                         interleaving: InterleavingMode, channel_name: Channel, code: CodeType, decoding_type: str):
    """Wpisuje do pliku ile dekodowan sie powiodlo i ile nie
    Parametry:
        - channel_name: string
        - ber: float
        - total_blocks: int
        - count_decoded: int
        - count_failed: int"""
    # Code;Channel Name;With Interleaving;Channel Quality;BER;Block size;Total Blocks;Decoded Blocks;Failed Blocks;Success Ratio
    write_interleaving = "invalid"
    if interleaving == InterleavingMode.WITH_INTERLEAVING:
        write_interleaving = "YES"
    elif interleaving == InterleavingMode.WITHOUT_INTERLEAVING:
        write_interleaving = "NO"

    file_operations.write_decoding_ratio(code.value,channel_quality.value,ber,total_blocks,count_decoded,count_failed,block_size,channel_name.value,write_interleaving, decoding_type)

def noise_comparison_in_GEC_channel(bit_blocks, noise_bit_blocks,byte_blocks,noise_byte_blocks,start_state,k,p_to_good,p_to_bad,h,is_interlaced):
    errors_bit_list=compare_blocks(bit_blocks, noise_bit_blocks)
    total_bit_errors=sum(errors_bit_list)
    errors_byte_list=compare_blocks(byte_blocks, noise_byte_blocks)
    total_byte_errors=sum(errors_byte_list)
    file_operations.write_noise_comparison_bits_for_GEC(start_state, k, p_to_good, p_to_bad, h, len(bit_blocks) * len(bit_blocks[0]), total_bit_errors, len(bit_blocks), total_bit_errors / len(bit_blocks), is_interlaced)
    file_operations.write_noise_comparison_bytes_for_GEC(start_state, k, p_to_good, p_to_bad, h, len(byte_blocks) * len(byte_blocks[0]), total_byte_errors, len(byte_blocks), total_byte_errors / len(byte_blocks), is_interlaced)

def decoder_success_rate_in_GEC_channel(start_state,k,p_to_good,p_to_bad, h, total_blocks,count_decoded,count_failed,is_interlaced):
    file_operations.write_decoding_ratio_for_GEC(start_state, k, p_to_good, p_to_bad, h, total_blocks, count_decoded, count_failed, is_interlaced)

def bits_group_errors_comparison(noise_byte_blocks, byte_blocks, is_interlaced):
    err_in_group=0
    error_groups = list()
    error_distance=0
    for i in range(len(byte_blocks)):
        for j in range(len(byte_blocks[0])):
            if byte_blocks[i][j] != noise_byte_blocks[i][j]:
                error_distance=0
                err_occured='true'
            else:
                error_distance+=1
                err_occured='false'
            if error_distance<=3 and err_occured=='true': err_in_group+=1
            if error_distance>3 and err_occured=='false':
                if err_in_group >= 3:  error_groups.append(err_in_group)
                err_in_group=0
    num_of_error_groups=len(error_groups)
    file_operations.write_bits_group_error_comparison(error_groups, num_of_error_groups, is_interlaced)

