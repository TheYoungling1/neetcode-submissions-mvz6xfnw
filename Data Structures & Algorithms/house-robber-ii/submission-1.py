class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # ah, so house 0 and house len(nums) - 1 are adjacent now 

        # if we use a bottom up approach, the house 0 will be filled first

        # if we use a tto

        # instead of having the dp_helper find the max amount from 0 to i house, we make it find the max amount from i to j house

        if len(nums) == 1:
            return nums[0]

        def rob_helper(nums):
            
            # we want to maximiase the amount of money we can rob

            # for our neighbours lets just look to the left neighbour for now

            # Input: nums = [2,9,8,3,6]

            # we can either rob 6 + max_rob(0:2), because we cant rob 3
            # we can also rob 3 instead +  max_rob(0:1), because then we also cant rob 8 or 6

            # all houses have positive money, so if we can never regress in amount if we rob a house 

            
            dp_list = [-1] * len(nums)
            # memorises to dp_list the max amount we can rob for houses betwen 0 to i
            def dp_helper(i):

                # even if we cache base cases in the dp array, it still will have O(1) lookup time
                if i < 0:
                    return 0

                if i == 0:
                    # only one house to rob
                    return nums[0]
                
                if i == 1:
                    return max(nums[0], nums[1])

                if dp_list[i] != -1:
                    return dp_list[i]
                
                dp_list[i] = max(nums[i] + dp_helper(i - 2), nums[i - 1] + dp_helper(i - 3))
                return dp_list[i]     
            

            return dp_helper(len(nums) - 1)
        
        return max(rob_helper(nums[1:]), rob_helper(nums[:-1]))
