class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0

        charSet = set()
        i = 0
        result = 0
        for j in range(len(s)):
            while s[j] in charSet:
                charSet.remove(s[i])
                i += 1
            charSet.add(s[j])
            result = max(result, j - i +1)
        return result
