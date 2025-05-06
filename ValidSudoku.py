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


        # Step 3: Check squares
        square_check = {}
        for row in range(len(board)):
            for col in range(len(board[row])):
                # If the current item is a dot, skip it
                if board[row][col] == ".":
                    continue
                # Get current square
                curr_square = (row // 3) * 3 + (col // 3)
                value = board[row][col]

                # Initialize this square if it doesn't exist
                if curr_square not in square_check:
                    square_check[curr_square] = {}

                # Check if value is in our square
                if value in square_check[curr_square]:
                    print("duplicate found in SQUARES")
                    return False
                else:
                    square_check[curr_square][value] = 1

        print("========= Square Check Clear =========")

        return True

if __name__ == "__main__":
    solution = Solution()
    
    # ANSI color codes
    RED = '\033[91m'
    GREEN = '\033[92m'
    RESET = '\033[0m'
    
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

    # Test Case 3 - Invalid Sudoku
    board3 = [
        [".",".","4",".",".",".","6","3","."],
        [".",".",".",".",".",".",".",".","."],
        ["5",".",".",".",".",".",".","9","."],
        [".",".",".","5","6",".",".",".","."],
        ["4",".","3",".",".",".",".",".","1"],
        [".",".",".","7",".",".",".",".","."],
        [".",".",".","5",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."],
        [".",".",".",".",".",".",".",".","."]
    ]
    
    # Test Case 1
    result1 = solution.isValidSudoku(board1)
    if result1 != True:
        print(f"{RED}Test Case 1 Failed! Expected: True, Got: {result1}{RESET}")
    else:
        print(f"{GREEN}Test Case 1 Passed! Expected: True, Got: {result1}{RESET}")
    
    # Test Case 2
    result2 = solution.isValidSudoku(board2)
    if result2 != False:
        print(f"{RED}Test Case 2 Failed! Expected: False, Got: {result2}{RESET}")
    else:
        print(f"{GREEN}Test Case 2 Passed! Expected: False, Got: {result2}{RESET}")

    # Test Case 3
    result3 = solution.isValidSudoku(board3)
    if result3 != False:
        print(f"{RED}Test Case 3 Failed! Expected: False, Got: {result3}{RESET}")
    else:
        print(f"{GREEN}Test Case 3 Passed! Expected: False, Got: {result3}{RESET}")