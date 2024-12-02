import random
class GEC:
    def __init__(self):
        self.p_to_bad =0.0002 # prawdopodobieństwo przejscia na zły kanał
        self.p_to_good = 0.0002 # prawdopodobieństwo przejscia na dobry kanał
        self.k = 0.0003  # prawdobodobieństwo błędu w w dobrym kanale
        self.h = 0.02  # prawdobodobieństwo błędu w w złym kanale

    def simulation(self,start_state, bit_blocks):
        """Otrzymuje bloki bitow przesylane przez kanal i zwraca je z szumem
        Parametry:
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks po szumach"""
        return self.gec(start_state, bit_blocks[:])

    def gec(self,start_state, bit_blocks):
        state = start_state
        no_err = 0
        err_num = 0
        for i in range(len(bit_blocks)):
            bit_block = bit_blocks[i]
            temp_bitblock = ""
            for bit in bit_block:
                if state == "GOOD":
                    if random.random() <= self.k:
                        if bit == "0":
                            temp_bitblock += "1"
                            err_num += 1
                        else:
                            temp_bitblock += "0"
                            err_num += 1
                    else:
                        temp_bitblock += bit
                    if random.random() <= self.p_to_bad + self.p_to_good*err_num:
                        state = "BAD"
                        err_num = 0
                elif state == "BAD": #mała szansa zmienienia na dobry, szansa rosnie gdy pojawiają sie pod rząd bity bez błędów
                    if random.random() <= self.h:
                        if bit == "0":
                            temp_bitblock += "1"
                            err_num += 1
                        else:
                            temp_bitblock += "0"
                            err_num += 1
                    else:
                        temp_bitblock += bit
                        if err_num==1: no_err += 1
                    if random.random() <= self.p_to_good + self.p_to_bad*no_err:
                        state = "GOOD"
                        no_err = 0
                        err_num = 0
                    if err_num >1: err_num = 0

                else:
                    raise Exception("Incorrect state")
            bit_block = temp_bitblock
            bit_blocks[i]=bit_block
        return bit_blocks
