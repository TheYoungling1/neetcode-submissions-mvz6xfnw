class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp_list = [-1] * (len(cost) + 1)

        # minimise the cost
        # i'th element in cost = the cost to step on the ith floor 

        # however, we can start at either 0 or 1st floor

        # since all costs are positive, then stepping stepping 2 steps will always be more cheaper than going 1 step twice, because you land on 2 stairs

        memo = {}
        def dp(i):
            # when arriving at every floor, we pay a tax of cost[0], even if we start on it, we pay the tax
            if i == 0: return cost[0]
            if i == 1: return cost[1]
            if i in memo: return memo[i]
            # the total cost of going to floor i, is the price of landing on floor 1 + the min cost of going to a fllor possible or reaching fllor i
            memo[i] = cost[i] + min(dp(i-1), dp(i-2))   # ask for smaller answers
            return memo[i]
        # going to the final platform oesnt require a tax, so the cost of getting there is either the total cost of getting to the floor below it, or cost of getting 
        # 2 floors below it
        return min(dp(len(cost)-1), dp(len(cost)-2))


