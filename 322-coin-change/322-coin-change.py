class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        '''
        Fewest number of coins!
        Brute Force
        Record how many coins take to get every amount no bigger than the amount given.
        '''
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        
        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        
        return dp[amount] if dp[amount] != amount + 1 else -1
    
        '''
        T(n) = O(amount * len(coins))
        S(n) = O(amount)
        '''