class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # for every O, we consider the O's surrounding it, and see if its 
        # fully bounded by X by checking if all its dfs' reaches the border

        # if there is a gap, a dfs/bfs will always find the border

        ROWS, COLS = len(board), len(board[0])

        
        # for each O, we dfs's to find if there is a way to the boundaries

        def is_on_boundary(r, c, visited):
            # Base Case: If out of bounds or at an 'X' or already visited, stop this path
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or (r, c) in visited:
                return False
            
            # Mark current cell as visited
            visited.add((r, c))
            
            # Check if THIS cell is on the boundary
            found_boundary = (r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1)
            
            # Check all 4 neighbors
            # Using '|' (OR) ensures if ANY neighbor finds the boundary, it becomes True
            res1 = is_on_boundary(r + 1, c, visited)
            res2 = is_on_boundary(r - 1, c, visited)
            res3 = is_on_boundary(r, c + 1, visited)
            res4 = is_on_boundary(r, c - 1, visited)
            
            return found_boundary or res1 or res2 or res3 or res4

        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    if not is_on_boundary(r, c, set()):
                        board[r][c] = "X"
