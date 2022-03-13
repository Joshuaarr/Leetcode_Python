<h2><a href="https://leetcode.com/problems/container-with-most-water/">11. Container With Most Water</a></h2><h3>Medium</h3><hr><div><p>You are given an integer array <code>height</code> of length <code>n</code>. There are <code>n</code> vertical lines drawn such that the two endpoints of the <code>i<sup>th</sup></code> line are <code>(i, 0)</code> and <code>(i, height[i])</code>.</p>

<p>Find two lines that together with the x-axis form a container, such that the container contains the most water.</p>

<p>Return <em>the maximum amount of water a container can store</em>.</p>

<p><strong>Notice</strong> that you may not slant the container.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://s3-lc-upload.s3.amazonaws.com/uploads/2018/07/17/question_11.jpg" style="width: 600px; height: 287px;">
<pre><strong>Input:</strong> height = [1,8,6,2,5,4,8,3,7]
<strong>Output:</strong> 49
<strong>Explanation:</strong> The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> height = [1,1]
<strong>Output:</strong> 1
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == height.length</code></li>
	<li><code>2 &lt;= n &lt;= 10<sup>5</sup></code></li>
	<li><code>0 &lt;= height[i] &lt;= 10<sup>4</sup></code></li>
</ul>
</div>


# Brute Force (TLE)
	class Solution:
	    def maxArea(self, height: List[int]) -> int:
		maxV = 0
		n = len(height)
		i = 0
		while i < n:
		    j = n - 1
		    while j > i:
			Volumn = min(height[i],height[j]) * (j - i) # 改进点
			maxV = max(maxV, Volumn)
			j -= 1
		    i += 1
		return maxV

# Brute Force 改进 （TLE）
	class Solution:
	    def maxArea(self, height: List[int]) -> int:
		maxV = 0
		n = len(height)
		i = 0
		while i < n: 				# HERE
		    j = n - 1
		    while j > i:
			width = j - i
			if height[i] < height[j]: 	# 对比之后省去一次乘法，但还是超时
			    Volumn = height[i] * width
			    j = 0
			else:
			    Volumn = height[j] * width
			    j -= 1
			maxV = max(maxV, Volumn)
		    i += 1
		return maxV
不需要在 HERE 处对i进行遍历，哪边边短哪边缩进一位比较好， 也可以省去一次判断。

# Strink from two end (Accepted)
	class Solution:
	    def maxArea(self, height: List[int]) -> int:
		maxV = 0
		n = len(height)
		i = 0
		j = n - 1
		while i < n and j > 0:
		    width = j - i
		    if height[i] < height[j]:
			Volumn = height[i] * width
			i += 1
		    else:
			Volumn = height[j] * width
			j -= 1
		    maxV = max(maxV, Volumn)
		return maxV
