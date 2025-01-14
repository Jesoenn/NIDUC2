import numpy as np
import pyldpc
from utils import converter

class LDPC:
    def __init__(self, block_size_in_bits, seed=None):
        self.block_size_in_bits = block_size_in_bits          # długość słowa kodowego w bitach
        self.d_v = 5                                          # liczba jedynek w każdym wierszu macierzy H
        self.d_c = 10                                          # liczba jedynek w każdej kolumnie macierzy H
        self.seed = seed
        self.H, self.G = pyldpc.make_ldpc(self.block_size_in_bits, self.d_v, self.d_c, True, self.seed)
        
        #print(self.H.shape)
        #print(self.G.shape)
        self.original_bit_blocks = []
        self.encoded_bit_blocks = []
        self.encoded_bit_blocks_in_bits = []

        self.block_size, self.information_size = self.G.shape
        self.block_size = self.block_size // 8
        self.information_size = self.information_size // 8



    def decode(self, bit_blocks):
        """
        Dekodowanie bloków bitów

        Parametry:
        - bit_blocks: list -> string

        Zwraca:
        - bit_blocks - zdekodowana lista bloków bitów
        - success_ratio - stosunek poprawnie zdekodowanych bloków do wszystkich
        """
        bit_blocks = converter.ldpc_from_bits_to_float(bit_blocks)
        j=0
        for i in range(len(bit_blocks)):
            if(i % (len(bit_blocks)//10) == 0):
                print("Decoding is {}% done".format(j))
                j+=10
            bit_blocks[i] = np.array([np.float64(bit) for bit in bit_blocks[i]])
            bit_blocks[i] = pyldpc.decode(self.H, bit_blocks[i], snr=np.inf, maxiter = 10)
            bit_blocks[i] = bit_blocks[i][:(self.information_size*8)]
            bit_blocks[i] = ''.join(map(str,bit_blocks[i]))     #Konwersja np.array na string
            if not ("1" in bit_blocks[i] or "0" in bit_blocks[i]):
                raise Exception("Cos poza 1 i 0?")
        
        return bit_blocks
    
    def encode(self, bit_blocks):
        """
        Kodowanie bloków bitów

        Parametry:
        - bit_blocks: list -> string

        Zwraca:
        - encoded_bit_blocks_in_bits - zakodowana lista bloków bitów (w bitach - 0 1)
        - bit_blocks - zakodowana lista bloków bitów (w float -1 i 1)
        """
        print("Encoding...")
        self.original_bit_blocks = bit_blocks[:]
        for i in range(len(bit_blocks)):
            bit_blocks[i] = np.array([int(bit) for bit in bit_blocks[i]], dtype=np.uint8)
            bit_blocks[i] = pyldpc.encode(self.G, bit_blocks[i], snr=np.inf)
        self.encoded_bit_blocks = bit_blocks
        self.encoded_bit_blocks_in_bits = converter.ldpc_from_float_to_bits(self.encoded_bit_blocks)
        return self.encoded_bit_blocks_in_bits, bit_blocks
     
    def getSuccessRatio(self):
        """
        Zwraca stosunek poprawnie zdekodowanych bloków do wszystkich bloków
        """
        success = 0
        for i in range(len(self.original_bit_blocks)):
            if self.original_bit_blocks[i] == self.encoded_bit_blocks[i]:
                success += 1
        return success / len(self.original_bit_blocks)
