class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # all cells have water,
        # find the cell that cal reach both pacific and 

        # for each point, we can do a dfs that checks if the the point can reach
        # r = 0 or c = 0 (pacific)
        # and r = ROWS - 1 or c = COLS - 1 (atlantic)

        # choose dfs because we just want to find reachability, not reall the shortest
        # way to get their. also less space in a naviagtion quesiton like this
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(heights), len(heights[0])


        def dfs(r, c, reachable_set, prev_height):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in reachable_set or heights[r][c] < prev_height:
                return 

            reachable_set.add((r, c))
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                dfs(nr, nc, reachable_set, heights[r][c])
        

        pacific_set = set()
        atlantic_set = set()

        for c in range(0, COLS):
            dfs(0, c, pacific_set, heights[0][c])

        for c in range(0, COLS):
            dfs(ROWS - 1, c, atlantic_set, heights[ROWS - 1][c])
        
        for r in range(0, ROWS):
            dfs(r, 0, pacific_set, heights[r][0])

        for r in range(0, ROWS):
            dfs(r, COLS - 1, atlantic_set, heights[r][COLS - 1])
        
        result = pacific_set.intersection(atlantic_set)

        return list(result)