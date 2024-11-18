<<<<<<< HEAD
import random
class BSC:

    def __init__(self, ber_type):
        # typy kanalow transmisyjnych
        bit_error_rates = [6 / 100000, 2 / 1000, 2 / 100]  # dobry, sredni, slaby
        if ber_type == "GOOD":
            self.bit_error_rate = bit_error_rates[0]
        elif ber_type == "MEDIUM":
            self.bit_error_rate = bit_error_rates[1]
        elif ber_type == "BAD":
            self.bit_error_rate = bit_error_rates[2]
        else:
            raise Exception("BSC type error")

    def simulation(self, bit_blocks):
        """Otrzymuje bloki bitow przesylane przez kanal i zwraca je z szumem
        Parametry:
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks po szumach"""
        return self.noise(bit_blocks[:])

    def noise(self, bit_blocks):
        """Symulacja szumu w kanale na podstawie BER
        Parametry:
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks po szumach"""
        for i in range(len(bit_blocks)):
            temp_bit_list = ""
            bit_block=bit_blocks[i]
            for bit in bit_block:
                error_prob = random.random()
                if error_prob <= self.bit_error_rate:
                    bit="1" if bit == "0" else "0"
                temp_bit_list += bit
            bit_blocks[i]=temp_bit_list
=======
import random
class BSC:

    def __init__(self, ber_type):
        # typy kanalow transmisyjnych
        bit_error_rates = [6 / 100000, 2 / 1000, 2 / 100]  # dobry, sredni, slaby
        if ber_type == "GOOD":
            self.bit_error_rate = bit_error_rates[0]
        elif ber_type == "MEDIUM":
            self.bit_error_rate = bit_error_rates[1]
        elif ber_type == "BAD":
            self.bit_error_rate = bit_error_rates[2]
        else:
            raise Exception("BSC type error")

    def simulation(self, bit_blocks):
        """Otrzymuje bloki bitow przesylane przez kanal i zwraca je z szumem
        Parametry:
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks po szumach"""
        return self.noise(bit_blocks[:])

    def noise(self, bit_blocks):
        """Symulacja szumu w kanale na podstawie BER
        Parametry:
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks po szumach"""
        for i in range(len(bit_blocks)):
            temp_bit_list = ""
            bit_block=bit_blocks[i]
            for bit in bit_block:
                error_prob = random.random()
                if error_prob <= self.bit_error_rate:
                    bit="1" if bit == "0" else "0"
                temp_bit_list += bit
            bit_blocks[i]=temp_bit_list
>>>>>>> origin/main
        return bit_blocks