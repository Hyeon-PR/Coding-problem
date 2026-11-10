class Solution:
    def findBall(self, grid: list[list[int]]) -> list[int]:
        m = len(grid)
        n = len(grid[0])

        res = []
        for ball in range(n):
            pos = ball
            for row in range(m):
                if pos != n - 1 and grid[row][pos] == 1 and grid[row][pos + 1] == 1:
                    pos += 1
                elif pos != 0 and grid[row][pos] == -1 and grid[row][pos - 1] == -1:
                    pos -= 1
                else:
                    res.append(-1)
                    break
            else:
                res.append(pos)
        return res
