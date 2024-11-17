from reedsolo import RSCodec, ReedSolomonError


class RS:
    def __init__(self,corrections):
        self.rsc=RSCodec(corrections*2)

    def encode(self, byte_249_blocks): #list -> bytearray
        for i in range(len(byte_249_blocks)):
            byte_249_blocks[i]=self.rsc.encode(byte_249_blocks[i])
        return byte_249_blocks

    def decode(self, encoded_block):

        # [0] - the decoded (corrected) message
        # [1] - the decoded message and error correction code (which is itself also corrected)
        # [2] - the list of positions of the errata (errors and erasures)
        try:
            return self.rsc.decode(encoded_block)[0], True
        except ReedSolomonError:
            decoded_byte_block = bytearray()
            for i in range(len(encoded_block) - 6):
                decoded_byte_block.append(encoded_block[i])
            return decoded_byte_block, False