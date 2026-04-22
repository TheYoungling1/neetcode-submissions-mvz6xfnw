class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
    
        res = []
        subset = []

        def dfs(i):
            if i == len(nums):
                res.append(subset.copy())
                return
            
            # no need to append to the subset arr
            dfs(i + 1)
            # no need to backtrack becaseu no addition
            
            subset.append(nums[i])
            dfs(i + 1)
            subset.pop()

        dfs(0)

        return res