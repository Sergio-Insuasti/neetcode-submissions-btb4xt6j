class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()

        def dfs(perm):
            if len(perm) == len(nums):
                res.add(tuple(perm))
                return
            
            for i in range(len(nums)):
                if nums[i] != float("-inf"):
                    perm.append(nums[i])
                    nums[i] = float("-inf")
                    dfs(perm)
                    nums[i] = perm[-1]
                    perm.pop()
        dfs([])
        return list(res)