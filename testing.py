import file_operations


def compare_bit_blocks(bit_blocks, noise_bit_blocks):
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
    errors_list=compare_bit_blocks(bit_blocks, noise_bit_blocks)
    total_errors=0
    for error in errors_list:
        total_errors+=error
    file_operations.write_noise_comparison(channel,ber,len(bit_blocks)*len(bit_blocks[0]),total_errors,len(bit_blocks),total_errors/len(bit_blocks))