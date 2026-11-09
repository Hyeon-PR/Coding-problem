class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        org_cnt = len(nums)
        rmv_cnt = 0
        while val in nums:
            nums.remove(val)
            rmv_cnt += 1
        return org_cnt - rmv_cnt
