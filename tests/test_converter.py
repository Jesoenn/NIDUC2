import unittest
import numpy as np
from utils.converter import ldpc_from_bits_to_float, ldpc_from_float_to_bits

class TestConverter(unittest.TestCase):
    def test_ldpc_from_bits_to_float(self):
        # Przykładowe dane wejściowe
        bit_blocks = ["101", "010", "111", "000"]
        
        # Oczekiwane dane wyjściowe
        expected_float_blocks = [
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
            [-1.0, -1.0, -1.0]
        ]
        
        # Wywołanie funkcji
        float_blocks = ldpc_from_bits_to_float(bit_blocks)
        
        # Sprawdzenie, czy wynik jest zgodny z oczekiwaniami
        self.assertEqual(float_blocks, expected_float_blocks)

    def test_ldpc_from_float_to_bits(self):
        # Przykładowe dane wejściowe
        float_blocks = [
            [1.0, -1.0, 1.0],
            [-1.0, 1.0, -1.0],
            [1.0, 1.0, 1.0],
            [-1.0, -1.0, -1.0]
        ]
        
        # Oczekiwane dane wyjściowe
        expected_bit_blocks = ["101", "010", "111", "000"]
        
        # Wywołanie funkcji
        bit_blocks = ldpc_from_float_to_bits(float_blocks)
        
        # Sprawdzenie, czy wynik jest zgodny z oczekiwaniami
        self.assertEqual(bit_blocks, expected_bit_blocks)
    
    def test(self):
        bit_blocks = ["101", "010", "111", "000"]

        bit_blocks1 = ldpc_from_bits_to_float(bit_blocks)
        bit_blocks1 = ldpc_from_float_to_bits(bit_blocks1)

        self.assertTrue(np.array_equal(bit_blocks1, bit_blocks))

if __name__ == '__main__':
    unittest.main()