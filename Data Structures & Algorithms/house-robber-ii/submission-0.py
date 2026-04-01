class Solution:
    def rob(self, nums: List[int]) -> int:
        def hr1(numbers):
            rob, not_rob = 0, 0
            for num in numbers:
                rob, not_rob = not_rob + num, max(rob, not_rob)
            return max(rob, not_rob)

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]
        else:
            return max(hr1(nums[1:]), hr1(nums[:-1]))


        