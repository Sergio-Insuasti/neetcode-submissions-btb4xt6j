class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(largest):
            subarray = 1
            currSum = 0
            for n in nums:
                currSum += n
                if currSum > largest:
                    subarray += 1
                    if subarray > k:
                        return False
                    currSum = n
            return True

        l, r = max(nums), sum(nums)
        res = r
        while l <= r:
            mid = l + (r-l)//2
            if canSplit(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
        
        
            
        