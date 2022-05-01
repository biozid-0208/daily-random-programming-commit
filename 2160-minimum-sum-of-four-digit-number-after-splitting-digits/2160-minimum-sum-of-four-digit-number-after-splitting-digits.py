class Solution:
    def minimumSum(self, num: int) -> int:
        arr = []
        while num:
            arr.append(num%10)
            num = num // 10
        arr.sort()
        return (arr[0]*10 + arr[3]) + (arr[1]*10 + arr[2])
        
        