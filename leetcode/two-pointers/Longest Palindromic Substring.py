class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        A = [0] * n

        def sliding(start, end):
            half = 0
            while start >= 0 and end <= n - 1 and s[start] == s[end]:
                start -= 1
                end += 1
                half += 1
            return half

        max_idx = -1
        max_half = -1
        is_even = True
        for i in range(n):
            half = sliding(i, i + 1) - 1
            if max_half <= half:
                max_half = half
                max_idx = i
                is_even = True
            half = sliding(i, i) - 1
            if max_half < half:
                max_half = half
                max_idx = i
                is_even = False

        if is_even:
            return s[max_idx - max_half : max_idx + max_half + 2]
        else:
            return s[max_idx - max_half : max_idx + max_half + 1]


if __name__ == "__main__":
    sol = Solution()
    input_txt = "babad"
    print(sol.longestPalindrome(input_txt))
