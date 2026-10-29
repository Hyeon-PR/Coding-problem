class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)
        nums.sort()
        for x in range(n - 2):
            left = x + 1
            right = n - 1
            if x != 0 and nums[x - 1] == nums[x]:
                continue
            while left < right:
                triplet = [nums[x], nums[left], nums[right]]
                if sum(triplet) == 0:
                    ans.append(triplet)
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif sum(triplet) < 0:
                    left += 1
                else:
                    right -= 1
        return ans


if __name__ == "__main__":
    sol = Solution()
    nums = [-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0]
    print(sol.threeSum(nums))
