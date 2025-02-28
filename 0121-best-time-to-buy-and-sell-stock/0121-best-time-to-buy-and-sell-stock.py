class Solution(object):
    def maxProfit(self, prices):
        if prices == None or len(prices) == 0:
            return 0
        elif len(prices) == 1:
            return prices[0]
        curMin = prices[0]
        maxProfit = 0
        for x in range(len(prices)):
            if prices[x] < curMin:
                curMin = prices[x]
            else:
                if prices[x]-curMin > maxProfit:
                    maxProfit = prices[x]-curMin
        return maxProfit
        