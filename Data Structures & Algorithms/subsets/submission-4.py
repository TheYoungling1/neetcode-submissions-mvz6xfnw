class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #brute force would be n^2

        # we know every subset has min length 1 and max length n - 1
        # for each subset size, we take snippets of size "k" of the array until we reach of the end

        # a problem is that at each size, we are just spedning themost time just cycliung through theses arrays
        # so im thinking if there are potential solutions that builds or decomposes the nodes we've already seen into small chunks
        # so with recursion

        res = []
        subset = []

        # i is what index in the element we are inspecting right now
        def dfs(i):
            if i >= len(nums):
                # reached the end of the layers
                # add whats in the subset rn
                res.append(subset.copy())
                return
            
            # we include the i'th element
            subset.append(nums[i])
            dfs(i + 1)
            # backtrack, the not include the i'th element
            subset.pop()
            # the base case will now append the versio with no latest elements
            dfs(i + 1)
        
        dfs(0)

        return res