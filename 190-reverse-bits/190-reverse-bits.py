class Solution:
    def reverseBits(self, n: int) -> int:
        reverse = 0
        counter = 32
        while counter > 0:
            reverse = reverse << 1
            if (n & 1) == 1:
                reverse ^= 1
            n= n >> 1
            counter -= 1
        return reverse

        