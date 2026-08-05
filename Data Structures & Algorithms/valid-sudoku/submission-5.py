class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        if not board:
            return True
        for i in range(0, 9):
            # check for duplicates in rows
            row_set = set()
            for item in board[i]:
                if item == ".":
                    continue
                elif item in row_set:
                    return False
                row_set.add(item)
            # check for duplicates in columns
            col_set = set()
            for j in range(0, 9):
                if board[j][i] == ".":
                    continue
                elif board[j][i] in col_set:
                    return False
                col_set.add(board[j][i])
            # check for duplicates in 3x3 grids
            r = c = [0, 1, 2]
            if i % 3 != 0:
                continue
            for k in range(0, 9, 3):
                box_set = set()
                for num1 in r:
                    for num2 in c:
                        if board[k + num1][i + num2] == ".":
                            continue
                        elif board[k + num1][i + num2] in box_set:
                            return False
                        box_set.add(board[k + num1][i + num2])
        return True

# O(1) time technically since fixed size, but generally O(n^2) + O(n^2) + O(n^2) time complexity
# O(n) space since sets grow linearly
