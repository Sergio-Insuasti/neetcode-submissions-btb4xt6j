class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # use a default list
        res = defaultdict(list)
        # iterate through each word and make a counter
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord('a')] += 1
            res[tuple(counter)].append(s)
        return list(res.values())