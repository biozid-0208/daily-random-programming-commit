class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct = {}
        for i in range(len(nums)):
            if (dct.get(target-nums[i], -1) == -1):
                dct[nums[i]] = i
            else:
                return [dct.get(target-nums[i]), i]