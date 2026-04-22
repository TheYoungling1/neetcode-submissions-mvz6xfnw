class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # So initially what I'm thinking would be that at each decision we can either consider a point horizontally or we can also consider a point vertically 
        # And I guess for the base case we can just have a value passed through in the recursion function that dictates the length of the path we're on right now. If that length is more than or equal to the number of words then straightaway we can indicate that we reached the base case and we can end the recursion from there 

        # And my intuition is telling me that we had to do this recursive function n square times but that could be a bit inefficient given that the recursive function itself might likely be of n. The total time complexity might be upwards of n to the power of n cubed 
            

        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            # Base Case: Found the whole word
            if i == len(word):
                return True
            
            # Boundary checks & Character mismatch & Already visited
            if (r < 0 or c < 0 or 
                r >= ROWS or c >= COLS or 
                word[i] != board[r][c] or 
                (r, c) in path):
                return False

            # 1. Choose: Mark as visited
            path.add((r, c))
            
            # 2. Explore: 4 directions
            res = (dfs(r + 1, c, i + 1) or
                dfs(r - 1, c, i + 1) or
                dfs(r, c + 1, i + 1) or
                dfs(r, c - 1, i + 1))
            
            # 3. Un-choose: Backtrack (remove from visited)
            path.remove((r, c))
            return res

        # Start the search from every cell
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0): return True
        return False
                



