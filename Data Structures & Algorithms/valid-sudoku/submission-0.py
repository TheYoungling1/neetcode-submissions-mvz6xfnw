class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Greedily add the current num to the "seen" col and row sets

        # find a way to find based off coords which 3x3 square set we are in
        # divide the coords by 3 and take the quotient

# Create 9 distinct sets for rows, columns, and 3x3 grids
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        grid = [set() for _ in range(9)]

        for i in range(9):
            for j in range(9):
                num = board[i][j]
                
                # Use continue to skip empty cells
                if num == ".":
                    continue
                
                # Calculate the unique ID for the 3x3 sub-box

                # What vertical box we are in, and what horizontal box coord we are in
                box_id = (i // 3) * 3 + (j // 3)

                # Check if we've seen this number in this row, col, or box
                if (num in rows[i] or 
                    num in cols[j] or 
                    num in grid[box_id]):
                    return False
                
                # Add the number to our sets
                rows[i].add(num)
                cols[j].add(num)
                grid[box_id].add(num)

        return True