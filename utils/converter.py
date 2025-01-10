
def bits_to_bytes(bit_blocks):
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
        
        
def bytes_to_bits(byte_blocks):
        """
        Funkcja zamiany bajtow na bity.
        Parametery:
            - byte_blocks: list -> bytearray
            - bit_blocks: list -> string
        Zwraca:
            - bit_blocks
        """
        bitblock = ""
        bit_blocks=[]
        for byte_block in byte_blocks:
            for byte in byte_block:
                bitblock+=format(byte, '08b')
            bit_blocks.append(bitblock)
            bitblock=""
        return bit_blocks