class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        

        # use a slowered dfs approach

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c, current_distance):
            # 1. Base Case: Out of bounds or hit a wall
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or grid[r][c] == -1:
                return
            
            # 2. The "Better Path" Check (This replaces the visit set!)
            # If the distance we took to get here is WORSE or EQUAL to what is 
            # already written in this cell, we stop. It's a dead end.
            if current_distance > grid[r][c]:
                return
            
            # 3. Update the cell with our new, better distance
            grid[r][c] = current_distance
            
            # 4. Continue the DFS to neighbors, adding 1 to the distance
            dfs(r + 1, c, current_distance + 1)
            dfs(r - 1, c, current_distance + 1)
            dfs(r, c + 1, current_distance + 1)
            dfs(r, c - 1, current_distance + 1)



        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    dfs(r, c, 0)
