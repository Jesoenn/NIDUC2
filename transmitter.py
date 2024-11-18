from image_operations import get_image_bytes
from rs_coder import RS

class Transmitter:
    block_size = 249
    corrections = (int)((255-block_size)/2)
    def __init__(self):
        # zmienne do zbierania danych
        self.original_byte_blocks = []
        self.encoded_byte_blocks = []
        self.encoded_interlaced_byte_blocks = []
        self.encoded_interlaced_bit_blocks=[]
        self.image_size = []
        

    def prepare_to_transmit(self):
        """
        Pobranie bytearray pikseli ze zdjecia oraz wielkosc zdjecia
        Parametry:
            - image_bytes: bytearray
            - image_size: list
            - original_byte_blocks: list -> bytearray
        """
        image_bytes,self.image_size = get_image_bytes()
        print("Image length in bytes: ", len(image_bytes))
        self.original_byte_blocks = self.divide_to_byte_blocks(image_bytes)
        print("Image length in bytes after grouping: ", len(self.original_byte_blocks) * self.block_size)

    def divide_to_byte_blocks(self,image_bytes):
        """
        Formatowanie jednego bytearray na liste blokow bytearray, kazdy z (block_size) bajtami
        Parametry:
            - image_bytes: bytearray
            - byte_blocks: list -> bytearray
        Zwraca:
            - byte_blocks
        """
        byte_blocks = []
        block = bytearray()
        for byte in image_bytes:
            block.append(byte)
            if len(block) == self.block_size:
                byte_blocks.append(block)
                block = bytearray()

        #If last block is not empty, fill with 0
        if block:
            for i in range(self.block_size - len(block)):
                block.append(0)
            byte_blocks.append(block)
        return byte_blocks

    def interlace(self,byte_blocks):
        """
        Funkcja przeplotu bajtow pomiedzy blokami: z kazdego wiersza po kolei kolumnami.
        Parametery:
            - byte_blocks: list -> bytearray
            - byte_interlaced_byte_blocks: list -> bytearray
        Zwraca:
            - byte_interlaced_byte_blocks
        """
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
        """
        Funkcja zamiany bajtow na bity.
        Parametery:
            - byte_blocks: list -> bytearray
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks
        """
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
        rs = RS(self.corrections)
        self.encoded_byte_blocks = rs.encode(self.original_byte_blocks[:])