class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        f = 1
        s = 0
        p = 0
        if len(prices) < 2:
            return 0
        while(f< len(prices)):
            if prices[f] > prices[s]:
                p = max(p,prices[f] - prices[s])
            else:
                s = f
            f += 1
        return p
                
            
        