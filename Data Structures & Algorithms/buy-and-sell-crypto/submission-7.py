class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        '''
        max_profit = 0
        
        for i, b in enumerate(prices):
            for s in prices[i+1:]:
                max_profit = max(max_profit, s-b)

        return max_profit
        '''

        max_profit, b, s = 0, len(prices) - 2, len(prices) - 1

        while b >= 0 and s >= 0:
            print(prices[b], prices[s])
            max_profit = max(max_profit, prices[s]-prices[b])
            if prices[b] > prices[s]:
                s = b
            b -= 1
        
        return max_profit