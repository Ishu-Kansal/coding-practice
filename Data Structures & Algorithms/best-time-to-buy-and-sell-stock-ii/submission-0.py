class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        holdPrice = prices[0]
        profit = 0

        for price in prices:
            # print(holdPrice, price)
            if(price < holdPrice):
                holdPrice = price
                hold = 1
            else:
                profit += price - holdPrice
                holdPrice = price
        
        return profit
            