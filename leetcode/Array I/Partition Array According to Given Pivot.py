class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        left = []
        equal = []
        right = []
        for num in nums:
            if num > pivot:
                right.append(num)
            elif num < pivot:
                left.append(num)
            else:
                equal.append(num)
        return left + equal + right
