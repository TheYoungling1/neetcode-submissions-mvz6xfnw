class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # matrix graph traversal problem

        # dfs/bfs

        #base case would be if we reach -1, stop

        ROWS, COLS = len(grid), len(grid[0])
        q = deque()
        
        # 1. Multi-Source Setup: Find all 0s and put them in the queue.
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    q.append((r, c))
                    # They are effectively "visited" because they are 0, not -1
        
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        # 2. Process the queue level by level
        while q:
            r, c = q.popleft()
            
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                
                # Check boundaries AND check if it's an unvisited empty room (-1)
                # If it's already a 0, or already has a positive distance, we skip it!
                if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 2147483647):
                    
                    # 3. Calculate distance and "mark visited" by mutating the grid
                    # The distance is simply the current cell's distance + 1
                    grid[nr][nc] = grid[r][c] + 1
                    
                    # 4. Add to queue ONLY after marking it visited
                    q.append((nr, nc))
                    
                

            
