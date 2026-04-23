class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] = the cost of landing on floor i + 1

        # in our dp list, dp[0] is going to represent the initial "ground" floor we are standing on

        # so in our first action, since we can only jump to floor 1 (get hit with cost[1 - 1]  = cost[0]) or floor 2 (get hit with cost[2 - 1] = cost[1])

        # so we are technically still "starting" at index 1 or index 0 in cost, by adding the ground floor, the logic of cost of leaving i is now equivilant as the logic of arriving at floor i 

        dp = [-1]*(len(cost) + 1) 

        # dp_list[i] the cost it takes to get to floor 1, so it takes 0 cost to get to floor 0 (the initial starting floor)
        # and it takes no cost to get to the last floor, so no need for a dedicated spot on the dp lit for both

        dp[0] = 0
        dp[1] = cost[0]
        dp[2] = cost[1]

        for i in range(3, len(cost) + 1):
            dp[i] = cost[i - 1] + min(dp[i - 1], dp[i - 2])

        return min(dp[len(cost)], dp[len(cost)- 1])

