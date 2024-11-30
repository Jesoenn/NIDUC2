import random
class GEC:
    def __init__(self):
        self.b_no_err_to_good = 20  # ilosc bitów bez błędów, która wymusza zmianę kanału na GOOD
        self.k = 0.0003  # prawdobodobieństwo błędu w w dobrym kanale
        self.h = 0.05  # prawdobodobieństwo błędu w w złym kanale

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
                if state == "GOOD": #zmienia się na zły kanał po pojawieniu się 1 błędu
                    if random.random() <= self.k:
                        if bit == "0":
                            temp_bitblock += "1"
                            state="BAD"
                        else:
                            temp_bitblock += "0"
                            state="BAD"
                    else:
                        temp_bitblock += bit
                elif state == "BAD": #zmienia się na dobry kanał gdy
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
                    if no_err>= self.b_no_err_to_good:
                        state = "GOOD"
                        no_err = 0
                        err_num = 0
                    if err_num >1: err_num = 0

                else:
                    raise Exception("Incorrect state")
            bit_block = temp_bitblock
            bit_blocks[i]=bit_block
        return bit_blocks
