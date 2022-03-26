class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maximum = 0
        for i, n in enumerate(accounts):
            curr = sum(n)
            if curr > maximum:
                maximum= curr
        return maximum
        