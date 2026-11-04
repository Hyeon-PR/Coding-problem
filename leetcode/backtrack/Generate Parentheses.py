class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        parenthesis = []

        def backtrack(i: int, j: int, temp: str):
            if i == n and j == n:
                parenthesis.append(temp)
                return
            if i > n or j > n:
                return

            backtrack(i + 1, j, temp + "(")
            if i > j:
                backtrack(i, j + 1, temp + ")")

        backtrack(1, 0, "(")
        return parenthesis


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        path = []  # 문자열 생성 메모리 최적화

        def backtrack(open_cnt: int, close_cnt: int):
            if len(path) == 2 * n:
                res.append("".join(path))
                return

            if open_cnt < n:
                path.append("(")
                backtrack(open_cnt + 1, close_cnt)
                path.pop()

            if close_cnt < open_cnt:
                path.append(")")
                backtrack(open_cnt, close_cnt + 1)
                path.pop()

        backtrack(0, 0)
        return res
