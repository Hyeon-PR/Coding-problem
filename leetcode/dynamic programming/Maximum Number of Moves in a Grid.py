from collections import deque


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        directions = [(-1, 1), (0, 1), (1, 1)]
        n, m = len(grid), len(grid[0])

        max_cnt = 0
        dq = deque()
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            dq.append((i, 0, 0))
            visited[i][0] = True
        while dq:
            cr, cc, cnt = dq.popleft()
            max_cnt = max(max_cnt, cnt)
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if (
                    0 <= nr < n
                    and 0 <= nc < m
                    and grid[nr][nc] > grid[cr][cc]
                    and not visited[nr][nc]
                ):
                    dq.append((nr, nc, cnt + 1))
                    visited[nr][nc] = True
        return max_cnt


class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        directions = [(-1, 1), (0, 1), (1, 1)]
        n, m = len(grid), len(grid[0])
        moves = [[-1] * m for _ in range(n)]
        for i in range(n):
            moves[i][0] = 0

        def dfs(cr, cc):
            cnt = moves[cr][cc]
            for dr, dc in directions:
                nr, nc = dr + cr, dc + cc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] > grid[cr][cc]:
                    if moves[nr][nc] == -1:
                        moves[nr][nc] = cnt + 1
                        dfs(nr, nc)
                    elif moves[nr][nc] <= cnt:
                        moves[nr][nc] = cnt + 1
                        dfs(nr, nc)
                    else:
                        continue

        for i in range(n):
            moves[i][0] = 0
            dfs(i, 0)
        return max(max(row) for row in moves)
