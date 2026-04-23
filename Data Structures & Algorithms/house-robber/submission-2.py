class Solution:
    def rob(self, nums: List[int]) -> int:
        
        # we want to maximiase the amount of money we can rob

        # for our neighbours lets just look to the left neighbour for now

        # Input: nums = [2,9,8,3,6]

        # we can either rob 6 + max_rob(0:2), because we cant rob 3
        # we can also rob 3 instead +  max_rob(0:1), because then we also cant rob 8 or 6

        # all houses have positive money, so if we can never regress in amount if we rob a house 

        
        dp_list = [-1] * len(nums)
        # memorises to dp_list the max amount we can rob for houses betwen 0 to i
        def dp_helper(i):
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


        

