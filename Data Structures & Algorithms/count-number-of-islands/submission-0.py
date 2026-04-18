class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        islands_found = 0

        # --- PART 2: The Recursive Sinker ---
        def sink_island(r, c):
            # Base cases: Stop recursing if we are out of bounds, 
            # or if we hit water ("0")
            if (r < 0 or r >= rows or 
                c < 0 or c >= cols or 
                grid[r][c] == "0"):
                return
            
            # We found land! Sink it immediately so we don't count it again.
            grid[r][c] = "0"
            
            # Recurse in all 4 directions
            sink_island(r + 1, c) # Down
            sink_island(r - 1, c) # Up
            sink_island(r, c + 1) # Right
            sink_island(r, c - 1) # Left

        # --- PART 1: The Outer Scanner ---
        for r in range(rows):
            for c in range(cols):
                # If we find an un-sunk piece of land...
                if grid[r][c] == "1":
                    islands_found += 1     # Count the new island!
                    sink_island(r, c)      # Launch the DFS to sink the rest of it

        return islands_found