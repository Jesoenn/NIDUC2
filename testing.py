import file_operations


def compare_bit_blocks(bit_blocks, noise_bit_blocks):
    """Porownanie kazdego kazdego bitu do siebie
    Parametry:
        - bit_blocks, noise_bit_blocks: list->string
        - block_changes: list->int
    Zwraca:
        - block_changes
    """
    block_changes = list()
    for i in range(len(bit_blocks)):
        for j in range(len(bit_blocks[0])):
            changes = 0
            original = noise_bit_blocks[i]
            noise = bit_blocks[i]
            if original[j] != noise[j]:
                changes += 1
            block_changes.append(changes)
    return block_changes

def noise_comparison(bit_blocks, noise_bit_blocks,channel,ber):
    """Porownuje dwa sygnaly i wpisuje do plikow wyniki
    Parametry:
        - bit_blocks, noise_bit_blocks: list->string"""
    errors_list=compare_bit_blocks(bit_blocks, noise_bit_blocks)
    total_errors=0
    for error in errors_list:
        total_errors+=error
    file_operations.write_noise_comparison(channel,ber,len(bit_blocks)*len(bit_blocks[0]),total_errors,len(bit_blocks),total_errors/len(bit_blocks))

def decoder_success_rate(channel_name, ber, total_blocks,count_decoded,count_failed):
    """Wpisuje do pliku ile dekodowan sie powiodlo i ile nie
    Parametry:
        - channel_name: string
        - ber: float
        - total_blocks: int
        - count_decoded: int
        - count_failed: int"""
    file_operations.write_decoding(channel_name,ber,total_blocks,count_decoded,count_failed)