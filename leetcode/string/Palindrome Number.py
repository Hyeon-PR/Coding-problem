class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        rev_s = s[::-1]
        return s == rev_s


if __name__ == "__main__":
    sol = Solution()
    x = 121
    print(sol.isPalindrome(x))
