class Solution(object):
    def minWindow(self, s, t):
        if not t or not s:
            return ""

        countT = Counter(t)
        window = Counter()

        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("inf")
        l = 0

        for r, c in enumerate(s):
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = r - l + 1

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l:r+1] if resLen != float('inf') else ""




