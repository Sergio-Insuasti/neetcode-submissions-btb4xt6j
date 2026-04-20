class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []

        size = len(matrix) * len(matrix[0])

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        while (len(result) < size):
            for i in range(left, right + 1):
                if len(result) < size:
                    result.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                if len(result) < size:
                    result.append(matrix[i][right])
            right -= 1

            for i in range(right, left - 1, -1):
                if len(result) < size:
                    result.append(matrix[bottom][i])
            bottom -= 1

            for i in range (bottom, top - 1, -1):
                if len(result) < size:
                    result.append(matrix[i][left])
            left += 1
        return result