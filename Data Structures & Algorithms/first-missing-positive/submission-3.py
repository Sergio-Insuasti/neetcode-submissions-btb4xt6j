class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Sol 1: Sorting -> O(nlogn)
        # nums.sort()
        # missing = 1
        # for num in nums:
        #     if num > 0 and missing == num:
        #         missing += 1
        # return missing
        
        # Sol 2: Negative Marking -> O(n)
        for i in range(len(nums)):
            if nums[i] < 0:
                nums[i] = 0
        
        for i in range(len(nums)):
            val = abs(nums[i])
            if 1 <= val <= len(nums):
                if nums[val - 1] > 0:
                    nums[val - 1] *= -1
                elif nums[val - 1] == 0:
                    nums[val - 1] = -1 * (len(nums) + 1)
        
        for i in range(1, len(nums) + 1):
            if nums[i-1] >= 0:
                return i
        
        return len(nums) + 1
            