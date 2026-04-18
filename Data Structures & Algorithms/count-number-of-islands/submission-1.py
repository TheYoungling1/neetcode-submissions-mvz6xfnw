class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # so the goal is that, everytime we see a "1", we want
        # to search the neighbours around it to check if they are also "1"
        # as then we can check if an "island" exists

        # when we visit an "1", we want to mark it as seen, so "0"
        # so it doesn't get explored again

        # for row 
        #     for col
        #         if grid[row][col] = 1:
        #             call recursive helper:
        #             island_count += 1
        #             (no only need to add once per "1" found)

        # recursive helper:
        #   dfs... bfs... algorithm, search for nearby "1" in up, down, left, right
        
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            # base case, if r, c is out of bounds or 0
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == "0"
            ):
                return

            # else, normal case, the grid is an island

            grid[r][c] = "0"

            dfs(r - 1, c)
            dfs(r + 1, c)
            dfs(r, c - 1)
            dfs(r, c + 1)


        islands = 0
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands
