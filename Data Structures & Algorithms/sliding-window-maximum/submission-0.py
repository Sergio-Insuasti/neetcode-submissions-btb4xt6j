class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        import heapq
        res = []
        i = 0
        j = i + k -1
        while j < len(nums):
            window = nums[i:j+1]
            res.append(max(window))
            i += 1
            j = i + k - 1
        return res