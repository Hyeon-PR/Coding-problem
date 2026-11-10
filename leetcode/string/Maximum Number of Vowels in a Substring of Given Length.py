class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        cur_vowels = sum(1 for c in s[:k] if c in vowels)
        max_vowels = cur_vowels

        for i in range(k, len(s)):
            if s[i] in vowels:
                cur_vowels += 1
            if s[i - k] in vowels:
                cur_vowels -= 1

            if cur_vowels > max_vowels:
                max_vowels = cur_vowels
                if max_vowels == k:
                    return k

        return max_vowels
