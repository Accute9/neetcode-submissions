class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs problem
        if not grid:
            return 0
        maxArea = 0
        rows, cols = len(grid), len(grid[0])
        def dfs(r, c):
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0
            if grid[r][c] != 1:
                return 0
            grid[r][c] = 9 # seen
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)      
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    curArea = dfs(r, c)
                    maxArea = max(maxArea, curArea)
                else:
                    continue
        return maxArea