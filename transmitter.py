from image_operations import get_image_bytes

class Transmitter:
    def prepare_to_transmit(self):
        """Returns list of bytearrays"""
        image_bytes = get_image_bytes()
        print("Image length in bytes: ", len(image_bytes))
        byte32_blocks = self.divide32byte(image_bytes)
        print("Image length in bytes after grouping: ", len(byte32_blocks) * 32)
        return byte32_blocks

    def divide32byte(self,image_bytes):
        """Formats one image bytearray to list of bytearrays, each with 32bytes"""
        byte32_blocks = []
        block = bytearray()
        for byte in image_bytes:
            block.append(byte)
            if len(block) == 32:
                byte32_blocks.append(block)
                block = bytearray()

        #If last block is not empty, fill with 0
        if block:
            for i in range(32 - len(block)):
                block.append(0)
            byte32_blocks.append(block)
        return byte32_blocks

    def interlace(self,byte32_blocks): #przeplot
        """Interlaces bytes from each block
            Parameter:
                byte32_blocks: list of bytearrays"""
        byte32_interlaced_blocks = []
        byte32_interlaced_block=bytearray()
        bytes_in_block=len(byte32_blocks[0])
        for i in range(bytes_in_block):
            for j in range(len(byte32_blocks)):
                byte32_interlaced_block.append(byte32_blocks[j][i]) #i position z j block32
                if len(byte32_interlaced_block) == bytes_in_block:
                    byte32_interlaced_blocks.append(byte32_interlaced_block)
                    byte32_interlaced_block=bytearray()
        return byte32_interlaced_blocks


