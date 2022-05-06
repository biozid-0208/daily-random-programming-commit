class Solution:
    def fib(self, n: int) -> int:
        a = 0
        b = 1
        if n <= 0:
            return 0
        
        for i in range(2,n+1):
            s = a + b
            a = b
            b = s
        return b
        