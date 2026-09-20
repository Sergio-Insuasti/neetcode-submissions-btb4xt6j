class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        for s in strs:
            freq = [0] * 26
            for c in s:
                freq[ord(c) - ord('a')] += 1
            freqarr = tuple(freq)
            if freqarr in anagrams:
                anagrams[freqarr].append(s)
            else:
                anagrams[freqarr] = [s]
        return list(anagrams.values())