class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])

        minHeap = [[0, 0, 0]]
        visit = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while minHeap:
            diff, r, c = heapq.heappop(minHeap)
            if (r, c) in visit:
                continue
            if r == ROWS - 1 and c == COLS - 1:
                return diff
            visit.add((r, c))
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if (
                    nr not in range(ROWS) or
                    nc not in range(COLS) or
                    (nr, nc) in visit
                ): continue
                newDiff = max(diff, abs(heights[r][c] - heights[nr][nc])) 
                heapq.heappush(minHeap, [newDiff, nr, nc])
