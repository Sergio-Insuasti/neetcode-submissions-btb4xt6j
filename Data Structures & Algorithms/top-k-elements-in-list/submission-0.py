class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import Counter
        n = len(nums)
        counter = Counter()

        for num in nums:
            counter[num] += 1

        return sorted(counter, key=lambda x: counter[x], reverse=True)[:k]
        