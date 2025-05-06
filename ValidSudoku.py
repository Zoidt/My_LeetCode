from typing import List

class Solution:

    # Only check for duplicates in row, column, and grid
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Step 1: Check Row
        for sublist in board:
            row_check = {}

            for item in sublist:
                if item == ".": 
                    continue
                if item in row_check:
                    print("duplicate found in ROWS") 
                    return False
                else:
                    row_check[item] = 1
                
        print("========= Row Check Clear =========")
        

        
        # Step 2: Check Column
        for i, sublist in enumerate(board):
            if sublist[i] == ".":
                continue

            col_check = {}

            if sublist[i] in col_check:
                print("duplicate found in COLUMNS")
                return False
            else:
                col_check[sublist[i]] = 1

        print("========= Col Check Clear =========")


        # Step 3: Check grid 
        # Check indexes here in loops of 3? 
        # Use formart board[i][j]
        # Formula

        return True

if __name__ == "__main__":
    solution = Solution()
    
    # Test Case 1 - Valid Sudoku
    board1 = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","8",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    # Test Case 2 - Invalid Sudoku
    board2 = [
        ["1","2",".",".","3",".",".",".","."],
        ["4",".",".","5",".",".",".",".","."],
        [".","9","1",".",".",".",".",".","3"],
        ["5",".",".",".","6",".",".",".","4"],
        [".",".",".","8",".","3",".",".","5"],
        ["7",".",".",".","2",".",".",".","6"],
        [".",".",".",".",".",".","2",".","."],
        [".",".",".","4","1","9",".",".","8"],
        [".",".",".",".","8",".",".","7","9"]
    ]
    
    print("Test Case 1 (Expected: True):", solution.isValidSudoku(board1))
    print("Test Case 2 (Expected: False):", solution.isValidSudoku(board2))