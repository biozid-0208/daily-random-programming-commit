class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = []
        
        for i in range(len(nums)):
            c = 0 
            for j in range(0, len(nums)):
                if nums[i] > nums[j] :
                    c += 1
            arr.append(c)
        return arr    
                