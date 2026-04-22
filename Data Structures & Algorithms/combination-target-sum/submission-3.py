class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # our baseline have to be if this "path" has overshot or right on the target

        # and since we can add each number infinite times, we for every recursion
        # for each num, we can choose to add it again, add a new num, or skip the current num 


        res = []
        subset = []

        def dfs(i, target):
            if target == 0:
                res.append(subset.copy())
                return
            elif i >= len(nums) or target < 0:
                return


            dfs(i + 1, target)
            # no need to add, no need to backtrack
            
            # subset.append(nums[i])
            # dfs(i + 1, target - nums[i])
            # subset.pop()

            subset.append(nums[i])
            dfs(i, target - nums[i])
            subset.pop() 

        dfs(0, target)

        return res