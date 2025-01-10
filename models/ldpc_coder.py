import numpy as np
import pyldpc 


class LDPC:
    def __init__(self, block_size_in_bits, parity_size, d_c, seed = None):
        self.block_size_in_bits = block_size_in_bits          #długość słowa kodowego w bitach
        self.parity_size = parity_size                        #liczba bitów parzystości
        self.d_c = d_c                                        #liczba bitów użytych w równaniu parzystości (musi być >= parity_size i musi dzielić block_size_in_bits) - bezpośrednio wpływa na złożoność obliczeniową.
        self.seed = seed
        self.H, self.G = pyldpc.make_ldpc(self.block_size_in_bits, self.parity_size, self.d_c, self.seed)
        
        self.original_bit_blocks = []
        self.encoded_bit_blocks = []
        

    def decode(self, bit_blocks):
        """
        Dekodowanie blokow bitow
        """
        for i in range(len(bit_blocks)):
            bit_blocks[i] = pyldpc.decode(self.H, bit_blocks[i], snr=np.inf)
        return bit_blocks, self.getSuccessRatio()
    
    def encode(self, bit_blocks):
        """
        Kodowanie blokow bitow
        """
        self.original_bit_blocks = bit_blocks
        for i in range(len(bit_blocks)):
            # Debugowanie typów danych
            # print(f"Typ danych bit_blocks[{i}]: {type(bit_blocks[i])}, wartość: {bit_blocks[i]}")
            # bit_blocks[i] = np.array(bit_blocks[i], dtype=int)  # Konwersja na numpy array z typem int             
            bit_blocks[i] = pyldpc.encode(self.G, bit_blocks[i], snr=np.inf)
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
        return success/len(self.original_bit_blocks)
        