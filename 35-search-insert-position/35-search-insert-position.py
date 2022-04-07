class Solution:
    def searchInsert(self, nums: List[int], t: int) -> int:
        l = 0
        h = len(nums)
        while l < h:
            m = l + ((h - l)//2)
            if nums[m] == t: 
                return m
            if nums[m] < t:
                l = m + 1
            else:
                h = m 
        return h
                
                
        
            
        