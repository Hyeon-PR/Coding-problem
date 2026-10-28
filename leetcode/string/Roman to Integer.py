class Solution:
    def romanToInt(self, s: str) -> int:
        num = 0
        RtoI = [
            ("M", 1000),
            ("CM", 900),
            ("D", 500),
            ("CD", 400),
            ("C", 100),
            ("XC", 90),
            ("L", 50),
            ("XL", 40),
            ("X", 10),
            ("IX", 9),
            ("V", 5),
            ("IV", 4),
            ("I", 1),
        ]
        for c, v in RtoI:
            n = len(c)
            while s[:n] == c:
                num += v
                s = s[n:]
            if s == "":
                break
        return num
