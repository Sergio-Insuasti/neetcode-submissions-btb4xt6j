class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        from collections import Counter

        counter = Counter()

        for c in s:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        counter2 = Counter()
        for c in t:
            if c not in counter:
                counter2[c] = 1
            else:
                counter2[c] += 1
        return counter==counter2
        