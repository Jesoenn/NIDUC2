import random
class BSC:

    def __init__(self, ber_type):
        bit_error_rates = [1 / 100000, 1 / 1000, 1 / 100]  # dobry, sredni, slaby
        if ber_type == "GOOD":
            self.bit_error_rate = bit_error_rates[0]
        elif ber_type == "MEDIUM":
            self.bit_error_rate = bit_error_rates[1]
        elif ber_type == "BAD":
            self.bit_error_rate = bit_error_rates[2]

    #dostaje z transmitter liste z bytearray na kazdym indeksie
    def bytes_to_bits(self, byte32_blocks):
        bitblock = ""
        bit256_blocks=[]
        for byteblock in byte32_blocks:
            for byte in byteblock:
                bitblock+=format(byte, '08b')
            bit256_blocks.append(bitblock)
            bitblock=""
        #48992 bajty, czyli 1531 blokow
        #32 bajty w bloku, czyli 32*8 bitow - 256
        return bit256_blocks

    def bits_to_bytes(self, bit_blocks):
        byte_32_blocks=[]
        for bit_block in bit_blocks:
            byteblock=bytearray()
            for i in range(0, len(bit_block), 8):
                byte=bit_block[i:i+8]
                byteblock.append(int(byte,2))
            byte_32_blocks.append(byteblock)
        return byte_32_blocks

    def receiver(self, byte32_blocks):
        bit_blocks=self.bytes_to_bits(byte32_blocks)
        # [:] przekazuje kopie
        bit_blocks_noise=self.noise(bit_blocks[:]) #TEST
        #self.compare_bitblocks(bit_blocks,bit_blocks_noise) #TEST
        test=self.bits_to_bytes(bit_blocks_noise)  #TEST

    # losuje czy dobry czy zly odbierze
    def noise(self, bit_blocks):
        for i in range(len(bit_blocks)):
            temp_bit_list = ""
            bit256block=bit_blocks[i]
            for bit in bit256block:
                error_prob = random.random()
                if error_prob <= self.bit_error_rate:
                    bit="1" if bit == "0" else "0"
                temp_bit_list += bit
            bit_blocks[i]=temp_bit_list
        return bit_blocks

    def compare_bitblocks(self, bit_blocks, bit_blocks2):
        zmiany = 0
        for i in range(len(bit_blocks2)):
            for j in range(256):
                str1 = bit_blocks2[i]
                str2 = bit_blocks[i]
                if str1[j] != str2[j]:
                    zmiany = zmiany + 1
        print(zmiany)

    def transmit(self):
        print(1)