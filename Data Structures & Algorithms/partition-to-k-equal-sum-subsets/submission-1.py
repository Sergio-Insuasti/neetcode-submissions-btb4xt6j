class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0: return False
        subsets = [0] * k
        target = sum(nums) // k

        def backtrack(i: int) -> bool:
            if i == len(nums): return True
            for j in range(k):
                if nums[i] + subsets[j] <= target:
                    subsets[j] += nums[i]
                    if backtrack(i + 1):
                        return True
                    else:
                        subsets[j] -= nums[i]
                    if subsets[j] == 0:
                        return False 
            return False
        return backtrack(0)

        # Question: can we divide a given list into subsets where
        # the sum of each are all equal??

        # hence each subset needs to have a sum equal to
        # TOTAL SUM // k

        # If the sum is not divisible -> return False

        # backtrack function (i)
        # if i == len(nums) -> True
        # maybe we loop through j (where j is nums 0 to k - 1)
        # if adding the current num will be <= target
        # we can then add and  