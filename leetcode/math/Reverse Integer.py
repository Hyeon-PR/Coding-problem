class Solution:
    def reverse(self, x: int) -> int:
        convert_x = str(x)
        if convert_x[0] == "-":
            ans_x = int("-" + convert_x[:0:-1])
        else:
            ans_x = int(convert_x[::-1])
        if -(1 << 31) <= ans_x <= (1 << 31) - 1:
            return ans_x
        else:
            return 0
