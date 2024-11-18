from rs_coder import RS
from image_operations import create_image
from transmitter import Transmitter
class Satellite:
    # zmienne do zbierania danych
    def __init__(self, image_size):
        self.encoded_bit_blocks = []
        self.encoded_byte_blocks = []
        self.decoded_byte_blocks = []
        self.image_size = image_size

    def receive_bit_blocks(self, bit_blocks):
        """Otrzymanie zakodowanych blokow bitow"""
        self.encoded_bit_blocks = bit_blocks

    def bits_to_bytes(self, bit_blocks):
        """
        Funkcja zamiany blokow bitow na bloki bajtow.
        Parametery:
            - bit_blocks: list -> string
            - byte_blocks: list -> bytearray
        Zwraca:
            - byte_blocks
        """
        byte_blocks = []
        for bit_block in bit_blocks:
            byte_block = bytearray()
            for i in range(0, len(bit_block), 8):
                byte = bit_block[i:i + 8]
                byte_block.append(int(byte, 2))
            byte_blocks.append(byte_block)
        return byte_blocks

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

    def decode(self):
        """Funkcja dekoduje blok po bloku, liczac ile dekodowan jest udanych i ile nie, a nastepnie tworzy zdjecie.
        Parametry:
            - count_decoded: int
            - count_failed: int
        Zwraca:
            - count_decoded, count_failed
        """
        self.decoded_byte_blocks=[]
        rs_decoder = RS(Transmitter.corrections)
        count_decoded=0
        count_failed=0
        for encoded_byte_block in self.encoded_byte_blocks:
            decoded_byte_block,decoded_success=rs_decoder.decode(encoded_byte_block, Transmitter.corrections)
            if decoded_success:
                count_decoded+=1
            else:
                count_failed+=1
            self.decoded_byte_blocks.append(decoded_byte_block)
        create_image(self.decoded_byte_blocks,self.image_size)
        return count_decoded,count_failed