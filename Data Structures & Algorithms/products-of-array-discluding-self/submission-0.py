class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        import math
        res = [1]*len(nums)

        for i in range(len(nums)):
           res[i] *= math.prod(nums[:i])

        for i in range(len(nums) - 1):
            res[i] *= math.prod(nums[i+1:len(nums)])

        return res
