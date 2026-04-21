class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        res = []
        subset = []

        candidates.sort()

        def dfs(i, target):

            if target == 0:
                # here is the problem 
                
                res.append(subset.copy())
                return

            if i >= len(candidates) or target < 0:
                return



            subset.append(candidates[i])
            dfs(i + 1, target - candidates[i])
            subset.pop()

            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            
            # Move to the next unique number
            dfs(i + 1, target)

    
        dfs(0, target)

        return res