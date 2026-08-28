class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        cumulative = [0] * len(nums)
        cumulative[0] = nums[0]
        for i in range(1, len(nums)):
            cumulative[i] = cumulative[i - 1] + nums[i]
        return cumulative
