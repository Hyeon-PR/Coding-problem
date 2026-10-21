class Solution:
    def convert(self, s: str, numRows: int) -> str:
        zigzag = [[] for _ in range(numRows)]
        idx = 0
        leng = len(s)
        row = 0
        inc = True
        if numRows == 1:
            return s
        while idx < leng:
            zigzag[row].append(s[idx])
            idx += 1
            if row == numRows - 1:
                inc = False
            if row == 0:
                inc = True
            if inc:
                row += 1
            else:
                row -= 1
        ans = ""
        for i in range(numRows):
            ans += "".join(zigzag[i])
        return ans


if __name__ == "__main__":
    sol = Solution()
    s = "PAYPALISHIRING"
    print(sol.convert(s, 3))
