class Solution:
    def reverseBits(self, n: int) -> int:
        bits = bin(n)
        bits = bits[2:].zfill(32)
        reversedbits = bits[::-1]
        return int(reversedbits,2)
        