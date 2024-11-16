from reedsolo import ReedSolomonError

from rs_coder import RS
from image_operations import create_image
class Satellite:
    def __init__(self):
        self.encoded_bit_blocks = []
        self.encoded_byte_blocks = []
        self.decoded_byte_blocks = []

    def receive_bit_blocks(self, bit_blocks):
        self.encoded_bit_blocks = bit_blocks

    def bits_to_bytes(self, bit_blocks):
        byte_blocks = []
        for bit_block in bit_blocks:
            byte_block = bytearray()
            for i in range(0, len(bit_block), 8):
                byte = bit_block[i:i + 8]
                byte_block.append(int(byte, 2))
            byte_blocks.append(byte_block)
        return byte_blocks

    def deinterlace(self,interlaced_byte_blocks):
        """Restore original data from interlaced blocks"""
        byte_blocks = []
        bytes_in_block = len(interlaced_byte_blocks[0])

        which_block=0
        for i in range(len(interlaced_byte_blocks)):
            for j in range(bytes_in_block):
                if len(byte_blocks)<len(interlaced_byte_blocks):
                    byte_blocks.append(bytearray())
                byte_blocks[which_block].append(interlaced_byte_blocks[i][j])
                which_block += 1
                if which_block==len(interlaced_byte_blocks):
                    which_block = 0
        return byte_blocks

    def decode(self):
        rs_decoder = RS(3)

        count_decoded=0
        count_failed=0
        for encoded_byte_block in self.encoded_byte_blocks:
            try:
                self.decoded_byte_blocks.append(rs_decoder.decode_array(encoded_byte_block))
                count_decoded += 1
            except ReedSolomonError:
                count_failed += 1
                decoded_byte_block=bytearray()
                for i in range(len(encoded_byte_block) - 6):
                    decoded_byte_block.append(encoded_byte_block[i])
                self.decoded_byte_blocks.append(decoded_byte_block)

        # TO GDZIES ZAPISAC
        print("ZDEKODOWANE " + str(count_decoded))
        print("NIEZDEKODOWANE " + str(count_failed))
        create_image(self.decoded_byte_blocks)