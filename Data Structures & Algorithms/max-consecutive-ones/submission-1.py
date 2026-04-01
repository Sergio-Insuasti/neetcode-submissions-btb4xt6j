class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        cur = 0
        
        for i in nums:
            if i == 1:
                cur += 1
            else:
                res = max(cur,res)
                cur = 0
        return max(cur,res)
        