class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def topologicalSort(edges: List[List[int]]) -> List[int]:
            neighbors = [[] for _ in range(k)]
            indegree = [0] * k
            for u, v in edges:
                neighbors[u - 1].append(v - 1)
                indegree[v - 1] += 1

            # use an array to record the row/col index for number 1~k
            indexes = [0] * k
            index = 0
            q = deque([i for i in range(k) if indegree[i] == 0])
            while q:
                current = q.popleft()
                indexes[current] = index
                index += 1
                for neighbor in neighbors[current]:
                    indegree[neighbor] -= 1
                    if indegree[neighbor] == 0:
                        q.append(neighbor)
        
            # if any of them has cycles, return []
            if index != k:
                return []
            return indexes
        
        rowIndexes = topologicalSort(rowConditions)
        if not rowIndexes:
            return []
        colIndexes = topologicalSort(colConditions)
        if not colIndexes:
            return []
        
        # put numbers on the matrix
        # O(m + n + k)/O(k^2)
        matrix = [[0] * k for _ in range(k)]
        for i in range(k):
            matrix[rowIndexes[i]][colIndexes[i]] = i + 1
        
        return matrix