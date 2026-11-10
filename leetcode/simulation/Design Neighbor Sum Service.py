class NeighborSum:

    def __init__(self, grid: List[List[int]]):
        self.adjacent = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.diagonal = [(-1, -1), (1, -1), (1, 1), (-1, 1)]
        self.grid = grid
        self.n = len(grid)

        self.pos = {
            grid[r][c]: (r, c) for r in range(self.n) for c in range(self.n)
        }

    def adjacentSum(self, value: int) -> int:
        total = 0
        cur_r, cur_c = self.pos[value]
        for dr, dc in self.adjacent:
            nxt_r, nxt_c = cur_r + dr, cur_c + dc
            if 0 <= nxt_r < self.n and 0 <= nxt_c < self.n:
                total += self.grid[nxt_r][nxt_c]
        return total

    def diagonalSum(self, value: int) -> int:
        total = 0
        cur_r, cur_c = self.pos[value]
        for dr, dc in self.diagonal:
            nxt_r, nxt_c = cur_r + dr, cur_c + dc
            if 0 <= nxt_r < self.n and 0 <= nxt_c < self.n:
                total += self.grid[nxt_r][nxt_c]
        return total

# Your NeighborSum object will be instantiated and called as such:
# obj = NeighborSum(grid)
# param_1 = obj.adjacentSum(value)
# param_2 = obj.diagonalSum(value)
