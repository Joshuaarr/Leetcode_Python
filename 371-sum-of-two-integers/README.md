<h2><a href="https://leetcode.com/problems/sum-of-two-integers/">371. Sum of Two Integers</a></h2><h3>Medium</h3><hr><div><p>Given two integers <code>a</code> and <code>b</code>, return <em>the sum of the two integers without using the operators</em> <code>+</code> <em>and</em> <code>-</code>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> a = 1, b = 2
<strong>Output:</strong> 3
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> a = 2, b = 3
<strong>Output:</strong> 5
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>-1000 &lt;= a, b &lt;= 1000</code></li>
</ul>
</div>



# binary 
	class Solution:
	    def getSum(self, a: int, b: int) -> int:
		mask = 0xffffffff 		# 用于处理负数情况
		while b & mask:
		    tmp = (a & b) << 1 		# 向左进位一位
		    a = (a ^ b) 
		    b = tmp 
		return (a & mask) if b > mask else a
		
1. 0x 是十六进制，每个 f 是二进制中的四个 1， 所以这里 mask 为二进制中的 32 个 1
2. and：& 为当同位都为 1 时取 1，其余情况取 0
3. xor：^ 为当同位相异时取 1，其余情况取 0

# Cheating method
	class Solution:
	    def getSum(self, a: int, b: int) -> int:
		return sum([a,b])
