from typing import List

class Solution1:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            try:
                pair = nums.index(target - nums[i], i + 1)
            except Exception:
                continue
            else:
                return [i, pair]
        return []

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in hashtable:
                return [i, hashtable[pair]]
            hashtable[nums[i]] = i
        return []