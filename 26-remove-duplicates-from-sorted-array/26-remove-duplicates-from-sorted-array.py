class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 1
        if len(nums) == 1 or nums == []:
            return 1
        while j < len(nums):
            if nums[j] != nums[j-1]:
                i += 1
                nums[i] = nums[j]
                j += 1
            else: 
                j += 1
        return i + 1
                
            
        