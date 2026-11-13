import math

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = defaultdict(set)
        columns = defaultdict(set)
        sub_boxes = defaultdict(set)

        for row in range(len(board)):
            for column in range(len(board[row])):
                if board[row][column] == ".":
                    continue
                sub_box = (math.floor(row/3), math.floor(column/3))
                if (board[row][column] in rows[row] or
                    board[row][column] in columns[column] or
                    board[row][column] in sub_boxes[sub_box]):
                    return False

                rows[row].add(board[row][column])
                columns[column].add(board[row][column])
                sub_boxes[sub_box].add(board[row][column])
        
        return True
                
                    
                
        
