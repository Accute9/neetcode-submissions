class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)
        ret_arr = []
        while left < right and top < bottom:
            # top row
            for i in range(left, right):
                ret_arr.append(matrix[top][i])
            top += 1
            # right column
            for i in range(top, bottom):
                ret_arr.append(matrix[i][right-1])
            right -= 1

            # prevent overlap
            if (right == left or top == bottom):
                break

            # bottom row
            for i in range(right-1, left-1, -1):
                ret_arr.append(matrix[bottom-1][i])
            bottom -= 1
            # left column
            for i in range(bottom-1, top-1, -1):
                ret_arr.append(matrix[i][left])
                print(top)
            left += 1
        return ret_arr

        # time complexity: O(m * n), every element traversed once, O(1) space