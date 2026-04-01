class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visit = set()
        minHeap = [[grid[0][0], 0, 0]]
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        visit.add((0,0))

        while minHeap:
            t, r, c = heapq.heappop(minHeap)
            if r == n - 1 and c == n - 1:
                return t
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr not in range(n) or
                    nc not in range(n) or
                    (nr, nc) in visit
                ): continue
                visit.add((nr, nc))
                heapq.heappush(minHeap, [max(t, grid[nr][nc]), nr, nc])