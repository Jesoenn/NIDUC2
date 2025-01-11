import numpy as np
import pyldpc

class LDPC:
    def __init__(self, block_size_in_bits, parity_size, d_c, seed=None):
        self.block_size_in_bits = block_size_in_bits          # długość słowa kodowego w bitach
        self.d_v = 3                                          # liczba jedynek w każdym wierszu macierzy H
        self.d_c = 6                                          # liczba jedynek w każdej kolumnie macierzy H
        self.seed = seed
        self.H, self.G = pyldpc.make_ldpc(self.block_size_in_bits, self.d_v, self.d_c, self.seed)
        
        self.original_bit_blocks = []
        self.encoded_bit_blocks = []

    def decode(self, bit_blocks):
        """
        Dekodowanie bloków bitów
        """
        for i in range(len(bit_blocks)):
            bit_blocks[i] = pyldpc.decode(self.H, bit_blocks[i], snr=np.inf)
        return bit_blocks, self.getSuccessRatio()
    
    def encode(self, bit_blocks):
        """
        Kodowanie bloków bitów
        """
        self.original_bit_blocks = bit_blocks
        for i in range(len(bit_blocks)):
            bit_blocks[i] = np.array([int(bit) for bit in bit_blocks[i]], dtype=np.uint8)
            bit_blocks[i] = pyldpc.encode(self.G.T, bit_blocks[i], snr=np.inf)
        self.encoded_bit_blocks = bit_blocks
        return bit_blocks
    
    def getG(self):
        return self.G
    
    def getH(self):
        return self.H
    
    def getSuccessRatio(self):
        """
        Zwraca stosunek poprawnie zdekodowanych bloków do wszystkich bloków
        """
        success = 0
        for i in range(len(self.original_bit_blocks)):
            if self.original_bit_blocks[i] == self.encoded_bit_blocks[i]:
                success += 1
        return success / len(self.original_bit_blocks)