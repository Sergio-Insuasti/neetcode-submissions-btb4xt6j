class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M':1000
        }

        result = 0

        for i, c in enumerate(s):
            result += romans[c]
            if (i + 1) != len(s) and romans[s[i + 1]] > romans[s[i]]:
                result -= 2 * romans[s[i]]
        return result