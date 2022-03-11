<h2><a href="https://leetcode.com/problems/maximum-product-subarray/">152. Maximum Product Subarray</a></h2><h3>Medium</h3><hr><div><p>Given an integer array <code>nums</code>, find a contiguous non-empty subarray within the array that has the largest product, and return <em>the product</em>.</p>

<p>The test cases are generated so that the answer will fit in a <strong>32-bit</strong> integer.</p>

<p>A <strong>subarray</strong> is a contiguous subsequence of the array.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [2,3,-2,4]
<strong>Output:</strong> 6
<strong>Explanation:</strong> [2,3] has the largest product 6.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [-2,0,-1]
<strong>Output:</strong> 0
<strong>Explanation:</strong> The result cannot be 2, because [-2,-1] is not a subarray.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 2 * 10<sup>4</sup></code></li>
	<li><code>-10 &lt;= nums[i] &lt;= 10</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>
</div>




# Brute Force (TLE)
	class Solution:
	    def maxProduct(self, nums: List[int]) -> int:
		n = len(nums)

		if n == 1:  #特殊情况
		    return nums[0]

		i = 0
		pro1 = nums[0]
		while i < len(nums): # 一位位遍历
		    j = i
		    pro2 = 1
		    while j < len(nums):
			pro2 *= nums[j]
			if pro2 >= 0 :
			    pro1 = max(pro1, pro2)
			j += 1
		    i += 1
		return pro1
		
# Save the current max and min (Accepted)
	class Solution:
	    def maxProduct(self, nums: List[int]) -> int:
		res = max(nums)				# 初始最大值设为 nums 中的最大值
		curMax, curMin = 1, 1

		for n in nums:
		    if n == 0:
			curMax, curMin = 1, 1 		# 当遇到 0 时重置 Max 和 Min 为 1
			continue
		    tmp = n * curMax 			# 注意在这里记录 n * curMax， 不然 curMin 那里用的是乘 n^2 的值
		    curMax = max(tmp, n * curMin, n)
		    curMin = min(tmp, n * curMin, n)
		    res = max(res, curMax)
		return res
        
