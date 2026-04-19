class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxx, minn = nums[0], nums[0]
        curMax, curMin = 0, 0
        total = 0

        for num in nums:
            curMax = max(curMax + num, num)
            curMin = min(curMin + num, num)
            total += num
            maxx = max(maxx, curMax)
            minn = min(minn, curMin)

        return max(maxx, total - minn) if maxx > 0 else maxx