class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board: return
        ROWS, COLS = len(board), len(board[0])
        
        # We'll store the coordinates of 'O's that we've confirmed ARE surrounded
        to_flip = []

        def can_escape(r, c, visited):
            # Base Case: Hit a wall or already searched this path
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or board[r][c] == 'X' or (r, c) in visited:
                return False
            
            # Base Case: We are standing on an 'O' that is on the boundary
            if r == 0 or r == ROWS - 1 or c == 0 or c == COLS - 1:
                return True
            
            visited.add((r, c))
            
            # Recursively check all directions
            # If ANY direction leads to an escape, this cell can escape
            return (can_escape(r + 1, c, visited) or
                    can_escape(r - 1, c, visited) or
                    can_escape(r, c + 1, visited) or
                    can_escape(r, c - 1, visited))

        # Brutally check every single cell
        for r in range(ROWS):
            for c in range(COLS):
                if board[r][c] == "O":
                    # Every time we find an 'O', we run a fresh search
                    # We use a brand new visited set so paths aren't blocked by old searches
                    if not can_escape(r, c, set()):
                        to_flip.append((r, c))
        
        # Finally, flip the ones that couldn't escape
        for r, c in to_flip:
            board[r][c] = "X"