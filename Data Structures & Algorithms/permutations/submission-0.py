class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        visited = [False]*len(nums)
        res = []

        def dfs(path):
            if len(path) == len(nums):
                res.append(path.copy())    
                return

            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    path.append(nums[i])
                    
                    # 2. Explore: Move to the next level of the tree
                    dfs(path)
                    
                    # 3. Backtrack: "Undo" the choice to try a different number
                    path.pop()
                    visited[i] = False                 
            

        dfs([])

        return res


        # for element, place it in first, then recursely find all possible options to fill the others with elements we havent seen before
