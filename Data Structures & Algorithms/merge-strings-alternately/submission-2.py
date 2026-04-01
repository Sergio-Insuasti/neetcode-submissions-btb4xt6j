class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        new_word = ""
        while i < len(word1) and j < len(word2):
            new_word += word1[i]
            new_word += word2[i]
            i += 1
            j += 1
        
        new_word += word1[i:]
        new_word += word2[j:]

        return new_word