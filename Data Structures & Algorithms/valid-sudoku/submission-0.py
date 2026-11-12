import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        sub_boxes = {}

        for row in range(len(board)):
            for column in range(len(board[row])):
                entry = board[row][column]
                sub_box = (math.floor(row/3), math.floor(column/3))
                if entry != ".":
                    entry = int(entry)
                    if row not in rows:
                        rows[row] = [0] * 9
                    if row in rows and entry == rows[row][entry-1]:
                        return False
                    rows[row][entry-1] = entry
                    if column not in columns:
                        columns[column] = [0] * 9
                    if column in columns and entry == columns[column][entry-1]:
                        return False
                    columns[column][entry-1] = entry
                    if sub_box not in sub_boxes:
                        sub_boxes[sub_box] = [0] * 9
                    if sub_box in sub_boxes and entry == sub_boxes[sub_box][entry-1]:
                        return False
                    sub_boxes[sub_box][entry-1] = entry
        return True
        
