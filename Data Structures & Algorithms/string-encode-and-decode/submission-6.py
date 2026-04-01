class Solution:

    def encode(self, strs: List[str]) -> str:
        # Create empty string res
        # Add the length of the upcoming string, a hash # and string s to res
        
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res
    
    def decode(self, s: str) -> List[str]:
        # Let the result be an empty list and i = 0
        res = []
        i = 0

        # while i is not at the end of s
        # we first set up a pointer i, and while j is not a #
        # traverse up s until we reach the #
        # The length is int(s[i:j])
        # Then set i to the next index and j to i + length
        # Append the word s[i:j] and append to res
        # Set i=j and return res when loop is complete

        while i < len(s):
            j = i
            
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length

            res.append(s[i:j])
            i = j
        return res
