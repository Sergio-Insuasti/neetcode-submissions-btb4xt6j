class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        path = [[0]*(n+1) for _ in range(m+1)]
        
        path[m-1][n-1] = 1
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                path[i][j] += path[i][j+1] + path[i+1][j]
        return path[0][0]
