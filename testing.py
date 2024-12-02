import file_operations

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

def noise_comparison(bit_blocks, noise_bit_blocks,byte_blocks,noise_byte_blocks,channel,ber):
    """Porownuje dwa sygnaly i wpisuje do plikow wyniki
    Parametry:
        - bit_blocks, noise_bit_blocks: list->string"""
    errors_bit_list=compare_blocks(bit_blocks, noise_bit_blocks)
    total_bit_errors=sum(errors_bit_list)
    errors_byte_list=compare_blocks(byte_blocks, noise_byte_blocks)
    total_byte_errors=sum(errors_byte_list)
    # Channel Name;BER;Total Bits;Total Bit Errors;Total blocks;Average Errors per Block
    file_operations.write_noise_comparison_bits(channel,ber,len(bit_blocks)*len(bit_blocks[0]),total_bit_errors,len(bit_blocks),total_bit_errors/len(bit_blocks))
    file_operations.write_noise_comparison_bytes(channel,ber,len(byte_blocks) * len(byte_blocks[0]),total_byte_errors,len(byte_blocks), total_byte_errors / len(byte_blocks))

def decoder_success_rate(channel_name, ber, total_blocks,count_decoded,count_failed):
    """Wpisuje do pliku ile dekodowan sie powiodlo i ile nie
    Parametry:
        - channel_name: string
        - ber: float
        - total_blocks: int
        - count_decoded: int
        - count_failed: int"""
    file_operations.write_decoding_ratio(channel_name,ber,total_blocks,count_decoded,count_failed)

def noise_comparison_in_GEC_channel(bit_blocks, noise_bit_blocks,byte_blocks,noise_byte_blocks,start_state,k,p_to_good,p_to_bad,h,is_interlaced):
    errors_bit_list=compare_blocks(bit_blocks, noise_bit_blocks)
    total_bit_errors=sum(errors_bit_list)
    errors_byte_list=compare_blocks(byte_blocks, noise_byte_blocks)
    total_byte_errors=sum(errors_byte_list)
    file_operations.write_noise_comparison_bits_for_GEC(start_state,k,p_to_good,p_to_bad,h,len(bit_blocks)*len(bit_blocks[0]),total_bit_errors,len(bit_blocks),total_bit_errors/len(bit_blocks),is_interlaced)
    file_operations.write_noise_comparison_bytes_for_GEC(start_state,k,p_to_good,p_to_bad,h,len(byte_blocks) * len(byte_blocks[0]),total_byte_errors,len(byte_blocks), total_byte_errors / len(byte_blocks),is_interlaced)

def decoder_success_rate_in_GEC_channel(start_state,k,p_to_good,p_to_bad, h, total_blocks,count_decoded,count_failed,is_interlaced):
    file_operations.write_decoding_ratio_for_GEC(start_state,k,p_to_good,p_to_bad,h,total_blocks,count_decoded,count_failed,is_interlaced)
