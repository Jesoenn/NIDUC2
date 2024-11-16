from reedsolo import RSCodec

class RS:
    def __init__(self,corrections):
        self.rsc=RSCodec(corrections*2)

    def encode(self, byte_249_blocks): #list -> bytearray
        for i in range(len(byte_249_blocks)):
            byte_249_blocks[i]=self.rsc.encode(byte_249_blocks[i])
        return byte_249_blocks

    #TEST
    def decode(self, encoded_blocks):
        decoded_blocks = []
        for block in encoded_blocks:
            # [0] - the decoded (corrected) message
            # [1] - the decoded message and error correction code (which is itself also corrected)
            # [2] - the list of positions of the errata (errors and erasures)
            decoded_blocks.append(self.rsc.decode(block)[0])
        return decoded_blocks