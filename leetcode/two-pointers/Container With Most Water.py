class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        start, end = 0, n - 1
        max_area = 0
        while start < end:
            if height[start] < height[end]:
                cur_h = height[start]
                area = cur_h * (end - start)
                start += 1
            else:
                cur_h = height[end]
                area = cur_h * (end - start)
                end -= 1
            max_area = max(max_area, area)
        return max_area


if __name__ == "__main__":
    sol = Solution()
    height = [1, 2, 1]
    print(sol.maxArea(height))
