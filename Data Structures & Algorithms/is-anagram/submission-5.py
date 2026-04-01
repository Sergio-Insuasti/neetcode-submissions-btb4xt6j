class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        list_s = list(s)
        for c in t:
            try:
                list_s.remove(c)
            except:
                return False
        return list_s == []
