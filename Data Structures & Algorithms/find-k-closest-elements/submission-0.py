class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        distances = {num: abs(num - x) for num in arr}
        sorted_nums = sorted(arr, key = lambda x: distances[x])
        return sorted(sorted_nums[:k])

            