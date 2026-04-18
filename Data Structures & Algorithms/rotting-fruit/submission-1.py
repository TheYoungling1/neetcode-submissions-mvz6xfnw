class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # basically a bfs that cecks how many 

        # its the algorithmically more similar to the questions, 
        # the fruits directly adjacent to the rotten fruits get rotten

        # we will initially put the rotten fruit in the queue, and add its neighbours
        
        # but how do we model a time tick?, we can do so by keeping a snapshot of the 
        # queue before adding neighbours, and increase the timetick until the snapshots all gone?

        # init queue

        # while queue:
        #   snapshot = len(queue)
        #   for snapshot:
        #       pop the head, add the infected neighbours if not infected already
        #   increment timer

        ROWS, COLS = len(grid), len(grid[0])
        queue = deque()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        num_fresh = 0

        for r in range(ROWS):   
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                if grid[r][c] == 1:
                    num_fresh += 1


        counter = 0
        rotten = False
        while queue:
            snapshot = len(queue)
            for _ in range(snapshot):
                r, c = queue.popleft()
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (0 <= nr < ROWS and 0 <= nc < COLS and grid[nr][nc] == 1):
                        grid[nr][nc] = 2
                        queue.append((nr, nc))
                        rotten = True
                        num_fresh -= 1
                
            
            if rotten:
                counter += 1
                rotten = False

        if num_fresh > 0:
            return -1
        return counter

        # 2 1 1
        # 0 1 1
        # 1 0 1
            

                
    
         
