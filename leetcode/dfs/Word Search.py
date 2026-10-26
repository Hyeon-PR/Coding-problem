class Solution:

    def exist(self, board: list[list[str]], word: str) -> bool:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n = len(board)
        m = len(board[0])
        visited = [[False] * m for _ in range(n)]

        def dfs(cur_r, cur_c, idx):
            if idx == len(word) - 1:
                return True

            visited[cur_r][cur_c] = True

            for dr, dc in directions:
                nxt_r, nxt_c = cur_r + dr, cur_c + dc
                if (
                    0 <= nxt_r < n
                    and 0 <= nxt_c < m
                    and not visited[nxt_r][nxt_c]
                    and board[nxt_r][nxt_c] == word[idx + 1]
                ):
                    if dfs(nxt_r, nxt_c, idx + 1):
                        return True

            visited[cur_r][cur_c] = False
            return False

        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0] and dfs(i, j, 0):
                    return True
        else:
            return False
