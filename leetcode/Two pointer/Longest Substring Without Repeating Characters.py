class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start, end = 0, 0
        sub = {}
        max_len = 1
        while end < len(s):
            cur = s[end]
            if cur not in sub or sub[cur] == 0:
                sub[cur] = 1
                end += 1
            else:
                while s[start] != cur:
                    sub[s[start]] -= 1
                    start += 1
                start += 1
                end += 1
            max_len = max(end - start, max_len)
        return max_len


if __name__ == "__main__":
    sol = Solution()
    s = "abcabcbb"
    print(sol.lengthOfLongestSubstring(s))
