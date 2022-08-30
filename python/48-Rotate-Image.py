class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        left, right = 0, len(matrix)-1

        while left < right:

            for i in range(right - left):
                top, bottom = left, right

                # assign top-left to a variable
                top_left = matrix[top][left + i]

                # assign bottom-left to top-left
                matrix[top][left + i] = matrix[bottom - i][left]

                # assign bottom-right to bottom-left
                matrix[bottom - i][left] = matrix[bottom][right - i]

                # assign top-right to bottom-right
                matrix[bottom][right - i] = matrix[top + i][right]

                # assign top-left to top-right
                matrix[top + i][right] = top_left

            left += 1
            right -= 1
