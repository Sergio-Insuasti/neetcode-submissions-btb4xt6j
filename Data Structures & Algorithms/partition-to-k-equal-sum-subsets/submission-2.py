class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0: return False
        subsets = [0] * k
        target = sum(nums) // k

        nums.sort(reverse=True)

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