class Solution:
    def climbStairs(self, n: int) -> int:
        dp_list = [-1]*(n + 1)


        def dp_loop(i):
            if i == 1:
                return 1
            if i == 2:
                return 2

            # check if this recursion has already been cached

            if dp_list[i] != -1:
                return dp_list[i]
            

            dp_list[i] = dp_loop(i - 1) + dp_loop(i - 2)

            return dp_list[i]

        
        return dp_loop(n)