<h2><a href="https://leetcode.com/problems/best-time-to-buy-and-sell-stock/">121. Best Time to Buy and Sell Stock</a></h2><h3>Easy</h3><hr><div><p>You are given an array <code>prices</code> where <code>prices[i]</code> is the price of a given stock on the <code>i<sup>th</sup></code> day.</p>

<p>You want to maximize your profit by choosing a <strong>single day</strong> to buy one stock and choosing a <strong>different day in the future</strong> to sell that stock.</p>

<p>Return <em>the maximum profit you can achieve from this transaction</em>. If you cannot achieve any profit, return <code>0</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> prices = [7,1,5,3,6,4]
<strong>Output:</strong> 5
<strong>Explanation:</strong> Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> prices = [7,6,4,3,1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> In this case, no transactions are done and the max profit = 0.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= prices.length &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= prices[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>

# Brute Force 1（TLE）
	class Solution:
	    def maxProfit(self, prices: List[int]) -> int:
		m = [0]
		c = 0
		for i in prices:
		    for j in prices[c+1::]:
			profit = j-i
			if profit not in m and profit > 0:
			    m.append(profit)
		    c += 1
		return max(m)
	
# Brute Force 2（TLE）
	class Solution:
	    def maxProfit(self, prices: List[int]) -> int:
		m = 0
		c = 0
		for i in prices:
		    for j in prices[c+1::]:
			profit = j-i
			if profit > m :
			    m = profit
		    c += 1
		return m

# Product from two ends (Submitted)
	class Solution:
	    def maxProfit(self, prices: List[int]) -> int:
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
