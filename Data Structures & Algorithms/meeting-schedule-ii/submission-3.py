"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        minh=[]
        intervals.sort(key=lambda i:i.start)
        for interval in intervals:
            s=interval.start
            e=interval.end
            if minh and s>=minh[0]:
                heapq.heappop(minh)
            heapq.heappush(minh,e)

        return len(minh)