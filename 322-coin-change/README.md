<h2><a href="https://leetcode.com/problems/coin-change/">322. Coin Change</a></h2><h3>Medium</h3><hr><div><p>You are given an integer array <code>coins</code> representing coins of different denominations and an integer <code>amount</code> representing a total amount of money.</p>

<p>Return <em>the fewest number of coins that you need to make up that amount</em>. If that amount of money cannot be made up by any combination of the coins, return <code>-1</code>.</p>

<p>You may assume that you have an infinite number of each kind of coin.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> coins = [1,2,5], amount = 11
<strong>Output:</strong> 3
<strong>Explanation:</strong> 11 = 5 + 5 + 1
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> coins = [2], amount = 3
<strong>Output:</strong> -1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> coins = [1], amount = 0
<strong>Output:</strong> 0
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= coins.length &lt;= 12</code></li>
	<li><code>1 &lt;= coins[i] &lt;= 2<sup>31</sup> - 1</code></li>
	<li><code>0 &lt;= amount &lt;= 10<sup>4</sup></code></li>
</ul>
</div>

# Brute Force (Botton up)
	class Solution:
	    def coinChange(self, coins: List[int], amount: int) -> int:
		'''
		Fewest number of coins!
		Brute Force
		Record how many coins take to get every amount no bigger than the amount given.
		'''

		dp = [amount + 1] * (amount + 1)
		dp[0] = 0
		'''
		Brute force through every coin and every amount
		Only record when the given coins are capable to reach the given amount
		'''
		for a in range(1, amount + 1):
		    for c in coins:		
			if a - c >= 0:
			    dp[a] = min(dp[a], 1 + dp[a - c])

		return dp[amount] if dp[amount] != amount + 1 else -1

		'''
		T(n) = O(amount * len(coins))
		S(n) = O(amount)
		'''
