import random
class BSC:

    def __init__(self, ber_type):
        bit_error_rates = [6 / 100000, 2 / 1000, 2 / 100]  # dobry, sredni, slaby
        if ber_type == "GOOD":
            self.bit_error_rate = bit_error_rates[0]
        elif ber_type == "MEDIUM":
            self.bit_error_rate = bit_error_rates[1]
        elif ber_type == "BAD":
            self.bit_error_rate = bit_error_rates[2]
        else:
            raise Exception("BSC type error")

    def simulation(self, bit_blocks):
        """Receives bits that go through the channel"""
        return self.noise(bit_blocks[:])

    def noise(self, bit_blocks):
        for i in range(len(bit_blocks)):
            temp_bit_list = ""
            bit_block=bit_blocks[i]
            for bit in bit_block:
                error_prob = random.random()
                if error_prob <= self.bit_error_rate:
                    bit="1" if bit == "0" else "0"
                temp_bit_list += bit
            bit_blocks[i]=temp_bit_list
        return bit_blocks






    #testowa funkcje
    def compare_bitblocks(self, bit_blocks, bit_blocks2):
        changes = 0
        for i in range(len(bit_blocks2)):
            for j in range(256):
                str1 = bit_blocks2[i]
                str2 = bit_blocks[i]
                if str1[j] != str2[j]:
                    changes += 1
        print(changes)

    def bits_to_bytes(self, bit_blocks):
        byte_32_blocks=[]
        for bit_block in bit_blocks:
            byteblock=bytearray()
            for i in range(0, len(bit_block), 8):
                byte=bit_block[i:i+8]
                byteblock.append(int(byte,2))
            byte_32_blocks.append(byteblock)
        return byte_32_blocks