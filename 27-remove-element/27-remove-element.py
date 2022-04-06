class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = -1
        j = 0
        if (len(nums) == 1 and nums[0] == val) or nums == []:
            return 0
        while j < len(nums):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
                j += 1
            else:
                j += 1
        return  i + 1 
                
                
        