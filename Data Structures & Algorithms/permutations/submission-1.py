class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res, perm = [], []
        def backtrack():
            if len(perm) == n:
                res.append(perm.copy())
                return
            for x in nums:
                if x not in perm:
                    perm.append(x)
                    backtrack()
                    perm.pop()
        backtrack()
        return res