<h2><a href="https://leetcode.com/problems/climbing-stairs/">70. Climbing Stairs</a></h2><h3>Easy</h3><hr><div><p>You are climbing a staircase. It takes <code>n</code> steps to reach the top.</p>

<p>Each time you can either climb <code>1</code> or <code>2</code> steps. In how many distinct ways can you climb to the top?</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> n = 2
<strong>Output:</strong> 2
<strong>Explanation:</strong> There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> n = 3
<strong>Output:</strong> 3
<strong>Explanation:</strong> There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= n &lt;= 45</code></li>
</ul>
</div>

# Bottom-up Dynamic Programming
	class Solution:
	    def climbStairs(self, n: int) -> int:
		a, b = 1, 1
		i = n - 1
		while i > 0:
		    num = a
		    a = num + b
		    b = num
		    i -= 1
		return a

If n = 5, and we start from floor 5:

			0 	1	 2 	3 	4 	5
	
1. Start from 5, there's 1 way to get 5.
2. Start from 4, there's 1 way to get 5.
3. Start from 3, you can take 1 step to 4 or 2 step to 5, and from 4 or 5, there's 1 way up to 5, so it's:
<pre>
	1 * 1 + 1 * 1 = 2 ways
</pre>
4. Start from 2, it's 1 step to 3 or 2 step to 4, and there's 2 way from 3 and 1 way from 4, so it's:
<pre>
	1 * 2 + 1 * 1 = 3 ways
</pre>	 
5. Start from 1, it's 1 step to 2 or 2 step to 3, and there's 3 way from 2 and 2 way from 3, so it's:
<pre>
	1 * 3 + 1 * 2 = 5 ways
</pre>	
6. Start from 0, it's 1 step to 1 or 2 step to 2, and there's 5 way from 1 and 3 way from 2, so it's:
<pre>
	1 * 5 + 1 * 3 = 8 ways
</pre>	 
Therefore, it's 8 ways in total from floor 0 to 5.
