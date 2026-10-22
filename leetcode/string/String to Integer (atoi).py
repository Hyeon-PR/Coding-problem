class Solution:
    def myAtoi(self, s: str) -> int:
        sub = ""
        for c in s:
            if sub == "" and c == " ":
                continue
            if sub == "" and c == "-":
                sub += "-"
                continue
            elif sub == "" and c == "+":
                sub += "+"
                continue
            if not ord("0") <= ord(c) <= ord("9"):
                break
            else:
                sub += c
        if sub == "":
            sub = "0"
        ans = 0
        if sub[0] == "-":
            minus = True
            leng = len(sub) - 1
            sub = sub[1:]
        else:
            minus = False
            leng = len(sub) if sub[0] != "+" else len(sub) - 1
            sub = sub if sub[0] != "+" else sub[1:]
        for i in range(leng):
            ans = ans * 10 + int(sub[i])
        if minus:
            ans = -ans
        if -(1 << 31) > ans:
            return -(1 << 31)
        elif ans > (1 << 31) - 1:
            return (1 << 31) - 1
        else:
            return ans


# Clean ver.
class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()  # Remove leading spaces
        if not s:
            return 0

        sign, i, res = 1, 0, 0

        # Check for sign
        if s[0] == "-":
            sign = -1
            i += 1
        elif s[0] == "+":
            i += 1

        while i < len(s) and s[i].isdigit():
            res = res * 10 + int(s[i])

            # Handle overflow
            if sign * res > 2**31 - 1:
                return 2**31 - 1
            if sign * res < -(2**31):
                return -(2**31)

            i += 1

        return sign * res
