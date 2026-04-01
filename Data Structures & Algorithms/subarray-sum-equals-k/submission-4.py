class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        summ = 0
        prefix_sums = {0: 1}
        for i in range(len(nums)):
            summ += nums[i]
            if summ - k in prefix_sums:
                res += prefix_sums[summ - k]
            prefix_sums[summ] = prefix_sums.get(summ, 0) + 1
        return res