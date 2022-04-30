class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ruuningSum = 0
        for i in range(len(nums)):
            ruuningSum += nums[i]
            nums[i] = ruuningSum
        return nums