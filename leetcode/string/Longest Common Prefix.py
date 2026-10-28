class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        prefix = ""
        idx = 0
        total = len(strs)
        is_valid = True
        while is_valid:
            try:
                for i in range(total):
                    if i == 0:
                        c = strs[i][idx]
                    else:
                        if c != strs[i][idx]:
                            is_valid = False
                            break
                    if i == total - 1:
                        prefix += c
                        idx += 1
            except Exception:
                is_valid = False
        return prefix
