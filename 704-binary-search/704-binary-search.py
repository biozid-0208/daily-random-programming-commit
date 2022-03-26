class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo  = 0
        hi = len(nums)-1
        while lo <= hi:
            mid = lo + (hi - lo)//2
            if nums[mid] == target:
                return mid
            if nums[mid] > target:
                hi = mid-1
            else:
                lo = mid+1
        return -1
        
            
        