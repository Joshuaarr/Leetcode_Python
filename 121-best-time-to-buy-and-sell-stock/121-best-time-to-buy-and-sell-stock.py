class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        思路：
        使用 left right 指针，左指针固定，右指针每次向后移一位
        每次循环比对，找最大的 profit
        当 diff 小于 0 时，更新左指针到右指针处

        特殊情况：
        len 为 1 时，输出 0
        '''
        profit = 0
        left = prices[0]
        for i in range(1, len(prices)):
            diff = prices[i] - left
            if diff > profit:
                profit = diff
            elif diff < 0:
                left = prices[i]
        return profit