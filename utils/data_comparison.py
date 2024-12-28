def compare_bytes(noise_byte_list: list, byte_list: list):
    rows = len(noise_byte_list)
    information_length = len(noise_byte_list[0])
    decoded_symbols = 0
    not_decoded_symbols = 0
    count_decoded_blocks = 0
    count_failed_blocks = 0
    for i in range(rows):
        block_decoded = True
        for j in range(information_length):
            if noise_byte_list[i][j] != byte_list[i][j]:
                if block_decoded:
                    block_decoded = False
                    count_failed_blocks+=1
                not_decoded_symbols += 1
            else:
                decoded_symbols += 1
        if block_decoded:
            count_decoded_blocks += 1
    return count_decoded_blocks, count_failed_blocks,decoded_symbols,not_decoded_symbols

