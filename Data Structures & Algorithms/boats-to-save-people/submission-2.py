class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        start, end, res = 0, len(people) - 1, 0
        while start <= end:
            remain = limit - people[end]
            end -= 1
            res += 1
            if start <= end and remain >= people[start]:
                start += 1
        return res
            
        