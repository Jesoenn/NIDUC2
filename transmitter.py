from image_operations import get_image_bytes
from rs_coder import RS

class Transmitter:
    # Przygotowanie bloków do transmisji
    def __init__(self):
        self.original_byte_blocks = []
        self.encoded_byte_blocks = []
        self.encoded_interlaced_byte_blocks = []
        self.encoded_interlaced_bit_blocks=[]
        self.image_size = []

    def prepare_to_transmit(self):
        """Returns list of bytearrays"""
        image_bytes,self.image_size = get_image_bytes()
        print("Image length in bytes: ", len(image_bytes))
        self.original_byte_blocks = self.divide_to_249_byte_blocks(image_bytes)
        print("Image length in bytes after grouping: ", len(self.original_byte_blocks) * 249)

    def divide_to_249_byte_blocks(self,image_bytes):
        """Formats one image bytearray to list of bytearrays, each with 249bytes"""
        byte_249_blocks = []
        block = bytearray()
        for byte in image_bytes:
            block.append(byte)
            if len(block) == 249:
                byte_249_blocks.append(block)
                block = bytearray()

        #If last block is not empty, fill with 0
        if block:
            for i in range(249 - len(block)):
                block.append(0)
            byte_249_blocks.append(block)
        return byte_249_blocks

    # Przeplot
    def interlace(self,byte_blocks):
        """Interlaces bytes from each block
            Parameter:
                byte_blocks: list of bytearrays, each has size of 255 bytes"""
        byte_interlaced_blocks = []
        byte_interlaced_block=bytearray()
        bytes_in_block=len(byte_blocks[0])
        for i in range(bytes_in_block):
            for j in range(len(byte_blocks)):
                byte_interlaced_block.append(byte_blocks[j][i]) #i position from j block
                if len(byte_interlaced_block) == bytes_in_block:
                    byte_interlaced_blocks.append(byte_interlaced_block)
                    byte_interlaced_block=bytearray()
        return byte_interlaced_blocks


    def bytes_to_bits(self, byte_blocks):
        bitblock = ""
        bit_blocks=[]
        for byte_block in byte_blocks:
            for byte in byte_block:
                bitblock+=format(byte, '08b')
            bit_blocks.append(bitblock)
            bitblock=""
        #255 bajtow w bloku, czyli 255*8 = 2040 bitow
        return bit_blocks

    def encode(self):
        rs = RS(3)
        self.encoded_byte_blocks = rs.encode(self.original_byte_blocks[:])