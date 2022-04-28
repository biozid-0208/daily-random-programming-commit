class Solution:
    def hammingWeight(self, n: int) -> int:
        r = 0
        while n > 0:
            if (n&1)==1:
                r +=1
            n = n >>1
        return r