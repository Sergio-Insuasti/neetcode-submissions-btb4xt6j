class Solution:
    def countBits(self, n: int) -> List[int]:
        def num_ones(n: int) -> int:
            return bin(n).count('1')
        
        res = []
        for i in range(n + 1):
            res.append(num_ones(i))
        return res