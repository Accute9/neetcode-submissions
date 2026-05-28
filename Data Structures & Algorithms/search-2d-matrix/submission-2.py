class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        low = 0 # first element of array
        row = len(matrix)
        col = len(matrix[0]) # m x n
        high = (row * col) - 1
        while low <= high:
            mid = (high + low) // 2
            row_idx = mid // col
            col_idx = mid % col
            if target > matrix[row_idx][col_idx]:
                # move low
                low = mid + 1
            elif target < matrix[row_idx][col_idx]:
                high = mid - 1
            else:
                return True
        return False


        # Time complexity: O(log(m * n)) - essentially runs binary search on the entire array
        # Space Complexity: O(1)
