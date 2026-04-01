class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] * n for  _ in range(n)]

        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        visit = set()

        def dfs(node):
            if node in visit:
                return True
            
            visit.add(node)
            for nei in graph[node]:
                dfs(nei)
            return False

        numC = 0
        for i in range(n):
            if not dfs(i):
                numC += 1
        return numC

