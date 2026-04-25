class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        # use the dp_list = stoe the least number of coins to  get to x amount


        # recursion, base case, the amount is < 0,
        # if the amount is 0, then return 1

        dp_list = {}

        def recursion(amount):
            if amount < 0:
                return float('inf')   # impossible — will never win the min
            if amount == 0:
                return 0              # base: zero coins to make zero
            if amount in dp_list:
                return dp_list[amount]
            
            min_global = float('inf')
            for coin in coins:
                min_global = min(min_global, 1 + recursion(amount - coin))
            
            dp_list[amount] = min_global
            return min_global

        result = recursion(amount)
        return result if result != float('inf') else -1