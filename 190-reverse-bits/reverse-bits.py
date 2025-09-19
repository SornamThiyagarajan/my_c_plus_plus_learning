class Solution:
    def reverseBits(self, n: int) -> int:
         # treat n as unsigned 32-bit
        n = n & 0xFFFFFFFF
        res = 0
        for _ in range(32):
            res = (res << 1) | (n & 1)
            n >>= 1
        # res is already in range 0..2^32-1
        return res