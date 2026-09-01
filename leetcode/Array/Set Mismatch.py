from typing import List


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        num_d = {i: 0 for i in range(1, len(nums))}
        error_num = [0, 0]
        for num in nums:
            num_d[num] += 1
        for num, occ in num_d.items():
            if occ == 2:
                error_num[0] = num
            elif occ == 0:
                error_num[1] = num
        return error_num
