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
		
收集所有大于 0 的 profit，然后返回最大的
	
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
		
设 m = 0，当 profit 大于 m 时，更新 m 的值

# Product from two ends (Submitted)
	class Solution:
	    def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		n = len(prices)
		#if n == 1 :		# 特殊情况，只有一天时，不买入不卖出，profit 为 0 （这一句不用，n = 1 的情况在下面会直接退出 while 循环输出 profit = 0）
		#    return profit
		i = 0
		left = prices[i] 	# 设置左右指针，当 diff 比 profit 大时，更新 profit，当 diff 小于 0 时，左指针移到右指针处。
		while i < n-1:		# 每个循环右指针后移一位。
		    i += 1
		    right = prices[i]
		    diff = right - left
		    if diff > profit :
			profit = diff
		    elif diff < 0 :
			left = right
		return profit
注意在这里指针的设置 left right 为具体的 value，而不是 index，这样可以避免每一个循环都重新查询一遍 left。
代码可精简为：
	class Solution:
	    def maxProfit(self, prices: List[int]) -> int:
		profit = 0
		left = prices[0]
		for r in range(1, len(prices)):
		    diff = prices[r] - left
		    if diff > profit:
			profit = diff
		    elif diff < 0:
			left = prices[r]
		return profit


