class Solution:
    def solve(self, board: List[List[str]]) -> None:
        
        # From brute force solution: O is not trapped if it has a way to reach
        # the boundary,

        # so, what if we transform this question to running dfs from the O's on the 
        # boundaries and see how many other O's it connects

        # To differentiate the O's reached by the boundry O's vs the ones truly 
        # trapped inside, we have a temp placeholder key "T". and at final, we simply
        # just transform T's into 'O' as they can can be reached, while making the O's
        # into 'X' as they are trapped

        ROWS, COLS = len(board), len(board[0])

        def helper(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] != "O":
                return
            
            # mark this tile as being reachable for a boundary O
            board[r][c] = "T"

            # recurse in 4 directions
            helper(r + 1, c)
            helper(r - 1, c)
            helper(r, c + 1)
            helper(r, c - 1)

        
        # cycle through the boundary O's in the board

        for c in range(0, COLS):
            if (board[0][c] == "O"):
                helper(0, c)
            
            if (board[ROWS - 1][c] == "O"):
                helper(ROWS - 1, c)
            
        for r in range(0, ROWS):
            if (board[r][0] == "O"):
                helper(r, 0)
            
            if (board[r][COLS - 1] == "O"):
                helper(r, COLS - 1)
        

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    board[r][c] = "X"

                if board[r][c] == "T":
                    board[r][c] = "O"
            
