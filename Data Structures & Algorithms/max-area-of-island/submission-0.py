class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # base case, if r, c is out of bounds or 0
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0
            ):
                return 0 

            # else, normal case, the grid is an island

            grid[r][c] = 0

            return 1 + dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)


        islands = 0
        curr_max = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    size = dfs(r, c)
                    if size > curr_max:
                        curr_max = size
        
        return curr_max