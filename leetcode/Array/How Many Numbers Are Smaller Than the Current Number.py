# Shortest Way
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        return [len([x for x in nums if x < num]) for num in nums]

# Fastest Way
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        cnt = [0] * 101
        cum = [0] * 101
        for n in nums:
            cnt[n] += 1
        cum[0] = cnt[0]
        for i in range(1, 101):
            cum[i] = cum[i - 1] + cnt[i]
        return [cum[n - 1] if n != 0 else 0 for n in nums]

