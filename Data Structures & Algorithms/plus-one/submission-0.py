class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits = list(map(str, digits))
        number = int("".join(digits))
        number += 1

        return [int(c) for c in str(number)]        