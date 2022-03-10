class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        profit = 0
        n = len(prices)
        if n == 1 :
            return profit
        i = 0
        left = prices[i]
        while i < n-1:
            i += 1
            right = prices[i]
            diff = right - left
            if diff > profit :
                profit = diff
            elif diff < 0 :
                left = right
        return profit
        