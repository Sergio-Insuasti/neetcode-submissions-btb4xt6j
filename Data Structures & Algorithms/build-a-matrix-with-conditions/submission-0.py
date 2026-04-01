class Solution:
    def buildMatrix(self, k: int, rowConditions: List[List[int]], colConditions: List[List[int]]) -> List[List[int]]:
        def top_sort(edges):
            inD = [0] * (k + 1)
            adj = [[] for _ in range(k + 1)]
            for u, v in edges:
                adj[u].append(v)
                inD[v] += 1
            
            order = []
            q = deque()
            for i in range(1, k + 1):
                if not inD[i]:
                    q.append(i)
            
            while q:
                node = q.popleft()
                order.append(node)
                for nei in adj[node]:
                    inD[nei] -= 1
                    if not inD[nei]:
                        q.append(nei)
            return order
        
        row_order = top_sort(rowConditions)
        if len(row_order) != k: return []
        col_order = top_sort(colConditions)
        if len(col_order) != k: return []
        
        res = [[0] * k for _ in range(k)]
        colIndex = [0] * (k + 1)
        for i in range(k):
            colIndex[col_order[i]] = i
        
        for i in range(k):
            res[i][colIndex[row_order[i]]] = row_order[i]
        return res