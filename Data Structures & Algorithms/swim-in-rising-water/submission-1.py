import heapq

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()
        
        # priority queue holds (current_max_elevation, row, col)
        # start with (grid[0][0], 0, 0)
        pq = [(grid[0][0], 0, 0)]
        
        while pq:
            # pop the cell with the smallest "max elevation along path"
            t, i, j = heapq.heappop(pq)
            
            # if we've reached the destination, return t
            # (your code here)
            if i == n - 1 and j == n - 1:
                return t
            
            # skip if already finalized
            # (your code here)
            if (i, j) in visited:
                continue
            
            # mark as finalized
            visited.add((i, j))
            
            # explore neighbors
            for di, dj in dirs:
                ni, nj = i + di, j + dj
                # check bounds and not visited
                # compute new_t = max(t, grid[ni][nj])
                # push (new_t, ni, nj) onto the priority queue
                if 0 <= ni < n and 0 <= nj < n and (ni, nj) not in visited:
                    new_t = max(t, grid[ni][nj])
                    heapq.heappush(pq, (new_t, ni, nj))
        
        return -1  # shouldn't reach here