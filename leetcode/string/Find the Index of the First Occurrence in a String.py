class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)  # Boyer-Moore 계열 O(N/M)


class Solution:  # KMP O(N + M)
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle:
            return 0

        # 1. LPS (Longest Prefix Suffix) 테이블 구축
        lps = [0] * len(needle)
        prev_lps, i = 0, 1
        while i < len(needle):
            if needle[i] == needle[prev_lps]:
                prev_lps += 1
                lps[i] = prev_lps
                i += 1
            elif prev_lps == 0:
                lps[i] = 0
                i += 1
            else:
                prev_lps = lps[prev_lps - 1]

        # 2. 텍스트 매칭 진행 (haystack 포인터 i는 절대 뒤로 되돌아가지 않음)
        i = j = 0  # i: haystack 포인터, j: needle 포인터
        while i < len(haystack):
            if haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                if j == 0:
                    i += 1
                else:
                    j = lps[j - 1]  # 이전 일치 접두사 위치로 점프

            if j == len(needle):
                return i - len(needle)

        return -1
