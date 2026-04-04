class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cache = {}
        
        def buyAndSell(i, bought):
            if i >= len(prices):
                return 0
            if (i,bought) in cache:
                return cache[(i,bought)]

            res = buyAndSell(i+1, bought)
            if bought:
                res = max(prices[i] + buyAndSell(i+2, False), res)
            else:
                res = max(buyAndSell(i+1, True) - prices[i], res)

            cache[(i,bought)] = res
            return res
            
        return buyAndSell(0, False)
        