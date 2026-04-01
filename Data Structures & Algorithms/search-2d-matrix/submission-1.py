class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        i, j = 0, len(matrix) - 1
        while i <= j:
            m = (i + j) // 2
            if matrix[m][0] <= target:
                i = m + 1
            else:
                j = m - 1

        if j < 0:
            return False

        targetRow = matrix[j]

        i, j = 0, len(targetRow) - 1
        while i <= j:
            m = (i + j) // 2
            if targetRow[m] == target:
                return True
            elif targetRow[m] < target:
                i = m + 1
            else:
                j = m - 1

        return False
