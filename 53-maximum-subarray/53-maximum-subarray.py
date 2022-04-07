class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cmax = nums[0] 
        tmax = nums[0] 
        i = 1
        while i < len(nums):
            if cmax < 0:
                cmax = nums[i]
                tmax = max(cmax, tmax)
            else:
                cmax += nums[i]
                tmax = max(cmax, tmax)
            i += 1
        return tmax
        