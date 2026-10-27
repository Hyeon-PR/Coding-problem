class Solution:
    def intToRoman(self, num: int) -> str:
        res = ""
        itoR = [
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
        for c, v in itoR:
            if c in ["I", "X", "C", "M"]:
                res += c * (num // v)
                num = num % v
            else:
                if num >= v:
                    res += c
                    num = num - v
            if num == 0:
                break
        return res
