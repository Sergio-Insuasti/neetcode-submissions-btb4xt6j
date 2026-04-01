class Solution:
    def numSquares(self, n: int) -> int:
        squares = []
        i = 1
        while i * i <= n:
            squares.append(i * i)
            i += 1

        memo = {}

        def dfs(total):
            if total == 0:
                return 0
            if total in memo:
                return memo[total]
            res = total
            for s in squares:
                if s > total:
                    break
                res = min(res, 1 + dfs(total - s))
            memo[total] = res
            return res

        return dfs(n)
            