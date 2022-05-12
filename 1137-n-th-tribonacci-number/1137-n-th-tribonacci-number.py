class Solution:
    def tribonacci(self, n: int) -> int:
        T0 = 0 
        T1 = 1
        T2 = 1
        if n <= 0:
            return 0
        if n < 3:
            return 1
        for i in range(3,n+1):
            T3 = T2 + T1+ T0
            T0 = T1
            T1 = T2
            T2 = T3
        return T3