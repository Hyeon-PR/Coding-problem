class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        n = len(nums)
        min_diff = float("inf")
        nums.sort()
        for x in range(n - 2):
            left = x + 1
            right = n - 1
            while left < right:
                sub_s = nums[x] + nums[left] + nums[right]
                diff = abs(sub_s - target)
                if diff < min_diff:
                    closest = sub_s
                    min_diff = diff
                if target > sub_s:
                    left += 1
                else:
                    right -= 1
        return closest
