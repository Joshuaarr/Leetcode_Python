<h2><a href="https://leetcode.com/problems/maximum-subarray/">53. Maximum Subarray</a></h2><h3>Easy</h3><hr><div><p>Given an integer array <code>nums</code>, find the contiguous subarray (containing at least one number) which has the largest sum and return <em>its sum</em>.</p>

<p>A <strong>subarray</strong> is a <strong>contiguous</strong> part of an array.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [-2,1,-3,4,-1,2,1,-5,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [4,-1,2,1] has the largest sum = 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [1]
<strong>Output:</strong> 1
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [5,4,-1,7,8]
<strong>Output:</strong> 23
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> &lt;= nums[i] &lt;= 10<sup>4</sup></code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> If you have figured out the <code>O(n)</code> solution, try coding another solution using the <strong>divide and conquer</strong> approach, which is more subtle.</p>
</div>

# Changing the start point
	class Solution:
	    def maxSubArray(self, nums: List[int]) -> int:
		n = len(nums)
		
		# 只有一个数字的情况
		if n == 1:
		    return nums[0]
		    
		# 不仅有一个数字的情况
		max_sol = cumsum = nums[0] 			# 初始值，最大解和连续和都为列表第一个数字
		for num in nums[1:]: #从第二个数字开始循环
		    if cumsum < 0 and num > cumsum: 		#如果之前的和小于0且num大于此和，则由num开始
			cumsum = num
		    else:
			cumsum += num
		    max_sol = max(max_sol, cumsum) 		#每一步后更新最大值！！
		return max_sol
