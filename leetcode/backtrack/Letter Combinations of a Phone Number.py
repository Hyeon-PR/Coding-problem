class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        digit_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }
        comb = []

        def backtrack(cur_idx: int, cur_comb: str):
            if cur_idx == len(digits):
                comb.append(cur_comb)
                return

            cand = digits[cur_idx]
            for c in digit_map[cand]:
                backtrack(cur_idx + 1, cur_comb + c)

        backtrack(0, "")
        return comb
