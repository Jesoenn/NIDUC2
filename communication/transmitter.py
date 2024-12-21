from common.code_type import CodeType
from common.interleaving_mode import InterleavingMode
from utils.image_operations import get_image_bytes
from models.rs_coder import RS
from common import interleaving_mode, code_type

class Transmitter:
    #block_size = 249
    #corrections = (int)((255-block_size)/2)
    def __init__(self):
        # zmienne do zbierania danych
        self.block_size = 0 # n (BYTES)
        self.information_size = 0 # k (BYTES)
        self.parity_size = 0 # n-k (BYTES)
        self.original_byte_blocks = []

        self.encoded_byte_blocks = []
        self.encoded_bit_blocks=[]

        self.encoded_interlaced_byte_blocks = []
        self.encoded_interlaced_bit_blocks=[]

        self.image_size = []
        self.image_bytes = bytearray()
        
    def get_image(self):
        self.image_bytes, self.image_size = get_image_bytes()

    def prepare_to_transmit(self, transmission_type: InterleavingMode, information_size: int, parity_size: int, chosen_code: CodeType):
        """
        Pobranie bytearray pikseli ze zdjecia oraz wielkosc zdjecia
        Parametry:
            - transmission_type: enum z common
            - block_size: int
            - image_bytes: bytearray
            - image_size: list
            - original_byte_blocks: list -> bytearray
        """
        self.information_size = information_size
        self.parity_size = parity_size
        self.block_size = information_size+parity_size
        self.original_byte_blocks = self.divide_to_byte_blocks(self.image_bytes) # podzielenie na bloki

        if chosen_code==CodeType.RS:
            self.rs_encode() # zakodowanie
        elif chosen_code==CodeType.LDPC:
            print("IN PROGRESS")

        if transmission_type == InterleavingMode.WITH_INTERLEAVING:
            self.encoded_interlaced_byte_blocks=self.interlace(self.encoded_byte_blocks[:])
            self.encoded_interlaced_bit_blocks=self.bytes_to_bits(self.encoded_interlaced_byte_blocks)
        elif transmission_type == InterleavingMode.WITHOUT_INTERLEAVING:
            self.encoded_bit_blocks=self.bytes_to_bits(self.encoded_byte_blocks)

    def print_info(self):
        print("Image length in bytes: ", len(self.image_bytes))
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
            if len(block) == self.information_size:
                byte_blocks.append(block)
                block = bytearray()

        #If last block is not empty, fill with 0
        if block:
            for i in range(self.information_size - len(block)):
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
        return bit_blocks


    def rs_encode(self):
        rs = RS(self.parity_size)
        self.encoded_byte_blocks = rs.encode(self.original_byte_blocks[:])