class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Initialise the full result array to 1s
        res = [1]*len(nums)

        # Multiply each entry in res by the product of all nums BEFORE i 
        for i in range(len(nums)):
           res[i] *= math.prod(nums[:i])

        # Multiply each entry in res by the product of all nums AFTER i
        for i in range(len(nums)):
            res[i] *= math.prod(nums[i+1:])

        # return res
        return res
