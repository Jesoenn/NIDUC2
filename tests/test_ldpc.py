import unittest
from models.ldpc_coder import LDPC
from utils.converter import ldpc_from_bits_to_float, ldpc_from_float_to_bits
import numpy as np
import pyldpc

class TestLDPC(unittest.TestCase):
    def setUp(self):
        # Inicjalizacja obiektu LDPC
        self.ldpc = LDPC(block_size_in_bits=2040)
        self.bit_blocks = ["1111111111111111111111111111111111111111111111111111110111111000111110001110010011100010111010111010000110111111111010101010000110111111111010101011100111001010111001111010000110111111111010101011100111001010111001111110001011101110111110001111110111111000111110001111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                           "1111111111111111111111111111111111111111111111111111111111101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110",
                           "1110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111",
                           "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110",
                           "1110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011101110111011111111111111111111111111111111111111111111111111111111111111111111111111111111"]
    
    def test(self):
        bit_blocks = self.bit_blocks[:]

        expected_decoded_bit_blocks = bit_blocks[:]

        transformed_bit_blocks, _ = self.ldpc.encode(bit_blocks[:])
        transformed_bit_blocks = self.ldpc.decode(transformed_bit_blocks)

        print(type(expected_decoded_bit_blocks))
        print(type(transformed_bit_blocks))

        self.assertTrue(np.array_equal(transformed_bit_blocks, expected_decoded_bit_blocks))
    
    def test_library(self):
        bit_blocks = self.bit_blocks[:]
        transformed_bit_blocks = self.bit_blocks[:]
        for i in range(len(bit_blocks)):
            transformed_bit_blocks[i] = np.array([int(bit) for bit in bit_blocks[i]], dtype=np.uint8)
            transformed_bit_blocks[i] = pyldpc.decode(self.ldpc.H, pyldpc.encode(self.ldpc.G, transformed_bit_blocks[i],snr = np.inf), snr = np.inf, maxiter=100)
            transformed_bit_blocks[i] = ''.join(map(str,bit_blocks[i]))
        self.assertTrue(np.array_equal(bit_blocks, transformed_bit_blocks))
    """
    def test_stupid(self):
        bit_blocks = self.bit_blocks
        bit_blocks2 = self.bit_blocks
        for i in range(len(bit_blocks)):
            bit_blocks[i] = np.array([int(bit) for bit in bit_blocks[i]], dtype=np.uint8)
            bit_blocks[i] = ''.join(map(str,bit_blocks[i]))

        self.assertTrue(np.array_equal(bit_blocks, bit_blocks2))
    """