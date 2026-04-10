class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Buy on the lowest day, sell on the highest

        # as the sell date is always later than the buy date

        left = 0
        right = 1

        max_profit = 0;

        while right < len(prices):

            curr = prices[right] - prices[left]

            if curr > max_profit:
                max_profit = curr

            # there is a cheaper day to buy
            if prices[right] < prices[left]:
                left = right
                
            right += 1
            
            
        
        return max_profit