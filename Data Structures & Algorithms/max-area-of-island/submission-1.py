class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        connectedComponents = []
        ROWS, COLS = len(grid), len(grid[0])
        maxArea = -float('inf')
        def dfs(r, c):
            perimeter = 1
            if (
                r < 0 or r >= ROWS or
                c < 0 or c >= COLS or
                grid[r][c] == 0
            ): return 0

            grid[r][c] = 0

            return perimeter + (
                dfs(r - 1,c) +
                dfs(r + 1,c) +
                dfs(r,c - 1) +
                dfs(r,c + 1)
            )
        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    connectedComponents.append(dfs(r,c))
        
        return max(connectedComponents) if connectedComponents else 0
            


        