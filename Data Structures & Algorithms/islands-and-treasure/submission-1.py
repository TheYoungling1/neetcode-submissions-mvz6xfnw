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
        
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        while q:
            node = q.popleft()

            for dir in direction:
                r, c = node[0] + dir[0], node[1] + dir[1]

                # node has not been visited (i.e. the value is still the very large val) and is in bound 
                if (0 <= r < ROWS and 0 <= c < COLS and grid[r][c] == 2147483647):
                    # ner value = 1 from the parent node

                    grid[r][c] = grid[node[0]][node[1]] + 1
                    q.append((r, c))


            
