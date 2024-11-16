from idlelib.configdialog import changes


def compare_bit_blocks(bit_blocks, noise_bit_blocks):
    block_changes = list()
    for i in range(len(bit_blocks)):
        changes=0
        for j in range(len(bit_blocks[0])):
            original = noise_bit_blocks[i]
            noise = bit_blocks[i]
            if original[j] != noise[j]:
                changes += 1
            block_changes.append(changes)
    return block_changes