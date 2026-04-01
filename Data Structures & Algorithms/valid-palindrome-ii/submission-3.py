class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            i, j = 0, len(s) -1 
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True
        if not s: return False
        if len(s) == 1: return True
        for i in range(len(s)):
            if isPalindrome(s[:i] + s[i+1:]):
                return True
        return False