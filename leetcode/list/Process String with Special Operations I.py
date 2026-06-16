class Solution:
    def processStr(self, s: str) -> str:
        lst = []
        for c in s:
            if c == "#":
                lst *= 2
            elif c == "%":
                lst.reverse()
            elif c == "*":
                if lst:
                    lst.pop()
            else:
                lst.append(c)
        return "".join(lst)
