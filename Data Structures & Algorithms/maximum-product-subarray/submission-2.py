class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #dp_list[i] keeps track of the largest and smallest value subgraph 
        # thats ending at i

        # so at i, we can either start a new subgraph, times the value right now
        # by the max/min product of subarray ending at i (depending on negative
        # or positive i)

        # 0 is covered by this algorithm i think

        dp_max = {}
        dp_min = {}

        def recursion(i):
            if i in dp_max:
                return (dp_max[i], dp_min[i])
            
            if i == 0:
                dp_max[i] = nums[i]
                dp_min[i] = nums[i]
                return (nums[i], nums[i])
    
            
            max_prev, min_prev = recursion(i - 1)
            max_end_here = max(nums[i], nums[i] * max_prev, nums[i] * min_prev)
            min_end_here = min(nums[i], nums[i] * max_prev, nums[i] * min_prev)

            dp_max[i] = max_end_here
            dp_min[i] = min_end_here

            return (max_end_here, min_end_here)

        # Prime the cache iteratively so the final call is shallow
        for i in range(len(nums)):
            recursion(i)
        
        return max(dp_max.values())

