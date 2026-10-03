class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness: int = 0
        for num in range(num1, num2 + 1):
            if num < 100:
                continue
            n: str = str(num)
            for mid in range(1, len(n) - 1):
                fr: int = int(n[mid - 1])
                md: int = int(n[mid])
                la: int = int(n[mid + 1])
                if (fr < md and la < md) or (fr > md and la > md):
                    waviness += 1
        return waviness

sol = Solution()
print(sol.totalWaviness(120, 130))
