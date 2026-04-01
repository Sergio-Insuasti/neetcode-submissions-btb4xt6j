class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False

        list_s = list(s)
        for ch in t:
            try:
                list_s.remove(ch)
            except:
                return False
        return list_s == []

