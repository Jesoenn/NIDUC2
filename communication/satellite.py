from common.channel_type import Channel
from common.code_type import CodeType
from common.interleaving_mode import InterleavingMode
from models.rs_coder import RS
from models.ldpc_coder import LDPC
from utils.image_operations import create_image
from common import code_type, interleaving_mode, channel_type
from utils import converter
class Satellite:
    # zmienne do zbierania danych
    def __init__(self, image_size, ldpc_H_matrix=None):
        self.encoded_bit_blocks = []
        self.encoded_byte_blocks = []
        self.encoded_interlaced_byte_blocks = []

        self.decoded_bit_blocks = []
        self.decoded_byte_blocks = []
        self.ldpc_H_matrix = []     # macierz H z kodu LDPC, potrzebna do dekodowania.
        self.image_size = image_size

    def receive_bit_blocks(self, bit_blocks, transmission_type: InterleavingMode, channel_used: Channel, code_used: CodeType, parity_size: int, ldpc_bites_in_equation: int | None=None):
        """Otrzymanie zakodowanych blokow bitow"""
        self.encoded_bit_blocks = bit_blocks # odbior bitow

        if code_used == CodeType.RS:
            self.encoded_byte_blocks=converter.bits_to_bytes(self.encoded_bit_blocks) # zamiana bitow na bajty
            if transmission_type == InterleavingMode.WITH_INTERLEAVING:
                self.encoded_interlaced_byte_blocks=self.encoded_byte_blocks[:]
                self.encoded_byte_blocks = self.deinterlace(self.encoded_byte_blocks)
            self.decode_rs(channel_used, parity_size)
        elif code_used == CodeType.LDPC:
            if transmission_type == InterleavingMode.WITH_INTERLEAVING:
                self.encoded_byte_blocks = converter.bits_to_bytes(self.encoded_bit_blocks)
                self.encoded_interlaced_byte_blocks=self.encoded_byte_blocks[:]
                self.encoded_byte_blocks = self.deinterlace(self.encoded_byte_blocks)
                self.encoded_bit_blocks = converter.bytes_to_bits(self.encoded_byte_blocks)
            self.decode_ldpc(parity_size, 3, ldpc_bites_in_equation)

    def deinterlace(self,interlaced_byte_blocks):
        """Zwraca oryginalny ciag wartosci z przeplotu
        Parametry:
            - interlaced_byte_blocks: list -> bytearray
            - byte_blocks: list -> bytearray
        Zwraca:
            - byte_blocks
        """
        byte_blocks = []
        bytes_in_block = len(interlaced_byte_blocks[0])
        which_block=0
        # po kolei wierszami i z kazdego wiersza przeplotu przepisuje do nowych wierszy
        # Przyklad: [0,0] do [0,0], [0,1] do [1,0], [0,2] do [2,0]
        for i in range(len(interlaced_byte_blocks)):
            for j in range(bytes_in_block):
                if len(byte_blocks)<len(interlaced_byte_blocks):
                    byte_blocks.append(bytearray())
                byte_blocks[which_block].append(interlaced_byte_blocks[i][j])
                which_block += 1
                if which_block==len(interlaced_byte_blocks):
                    which_block = 0
        return byte_blocks

    def decode_rs(self, channel_used, parity_size):
        """Funkcja dekoduje blok po bloku, liczac ile dekodowan jest udanych i ile nie, a nastepnie tworzy zdjecie.
        Parametry:
            - count_decoded: int
            - count_failed: int
        Zwraca:
            - count_decoded, count_failed
        """
        self.decoded_byte_blocks=[]
        rs_decoder = RS(parity_size)
        for encoded_byte_block in self.encoded_byte_blocks:
            decoded_byte_block,decoded_success=rs_decoder.decode(encoded_byte_block, parity_size)
            self.decoded_byte_blocks.append(decoded_byte_block)
        #create_image(self.decoded_byte_blocks,self.image_size, channel_used.value)

        self.decoded_bit_blocks = converter.bytes_to_bits(self.decoded_byte_blocks)

    def decode_ldpc(self, parity_size, ldpc_bites_in_equation):
        ldpc_decoder = LDPC(len(self.encoded_bit_blocks[0]), parity_size, ldpc_bites_in_equation)
        self.decoded_bit_blocks, decoded_success = ldpc_decoder.decode(self.encoded_bit_blocks)
        self.decoded_byte_blocks = converter.bits_to_bytes(self.decoded_bit_blocks)


