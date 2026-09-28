class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        length = len(prices) - 1
        buy = 0
        sell = 0
        maxProf = 0
        # Loop for i through length
        while i <= length:
            # Base case
            if i == 0 and buy == 0:
                buy = prices[i]

            # If its a profit if you sold this day
            elif prices[i] - buy > maxProf:
                maxProf = prices[i] - buy
            
            elif prices[i] < buy:
                buy = prices[i]

            i += 1
        return maxProf