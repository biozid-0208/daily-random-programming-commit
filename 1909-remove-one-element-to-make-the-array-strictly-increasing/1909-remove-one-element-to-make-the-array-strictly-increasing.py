class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return True
        firstPrev = 0
        secondPrev = 0
        error = 0
        for i in range(len(nums)):
            if nums[i]> firstPrev:
                secondPrev = firstPrev
                firstPrev = nums[i]  
            elif  nums[i] > secondPrev:
                error += 1
                firstPrev = nums[i] 
            else:
                error += 1
        return error < 2 


                

                
                

        
        