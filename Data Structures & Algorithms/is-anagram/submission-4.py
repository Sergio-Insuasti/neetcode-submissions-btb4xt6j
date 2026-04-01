class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        from collections import defaultdict

        d1 = defaultdict()
        for c in s:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1

        d2 = defaultdict()

        for c in t:
            if c not in d2:
                d2[c] = 1
            else:
                d2[c] += 1

        return d1 == d2
        