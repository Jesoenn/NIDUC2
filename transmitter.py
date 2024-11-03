from image_operations import get_image_bytes

class Transmitter:
    # otrzymuje kod
    # dzieli na bloki 32bajtowe - ostatni zapelnic zerami chyba
    # Koduje -> rs_coder
    # wysyla do BSC

    def prepare_to_transmit(self):
        image_bytes = get_image_bytes()
        print("DLUGOSC ZDJECIA W BAJTACH: ", len(image_bytes))
        byte32_blocks = self.divide32byte(image_bytes)
        print("DLUGOSC WYSYLU W BAJTACH: ", len(byte32_blocks) * 32)
        return byte32_blocks

    def divide32byte(self,image_bytes):
        byte32_blocks = []
        block = bytearray()
        for byte in image_bytes:
            block.append(byte)
            if len(block) == 32:
                byte32_blocks.append(block)
                block = bytearray()

        # jezeli ostatni blok nie jest pusty
        if block:
            for i in range(32 - len(block)):
                block.append(0)
            byte32_blocks.append(block)
        return byte32_blocks

    def interlace(self,byte32_blocks):
        #byte32_blocks list->bytearray->int
        byte32_interlaced_blocks = []
        byte32_interlaced_block=bytearray()
        for i in range(32): #tyle bajtow w bloku
            for j in range(len(byte32_blocks)): #tyle blokow
                byte32_interlaced_block.append(byte32_blocks[j][i]) #i'ta pozycja z j'tego bloku32
                if len(byte32_interlaced_block) == 32:
                    byte32_interlaced_blocks.append(byte32_interlaced_block)
                    byte32_interlaced_block=bytearray()
        return byte32_interlaced_blocks


