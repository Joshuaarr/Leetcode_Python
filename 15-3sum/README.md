<h2><a href="https://leetcode.com/problems/3sum/">15. 3Sum</a></h2><h3>Medium</h3><hr><div><p>Given an integer array nums, return all the triplets <code>[nums[i], nums[j], nums[k]]</code> such that <code>i != j</code>, <code>i != k</code>, and <code>j != k</code>, and <code>nums[i] + nums[j] + nums[k] == 0</code>.</p>

<p>Notice that the solution set must not contain duplicate triplets.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [-1,0,1,2,-1,-4]
<strong>Output:</strong> [[-1,-1,2],[-1,0,1]]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = []
<strong>Output:</strong> []
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [0]
<strong>Output:</strong> []
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>0 &lt;= nums.length &lt;= 3000</code></li>
	<li><code>-10<sup>5</sup> &lt;= nums[i] &lt;= 10<sup>5</sup></code></li>
</ul>
</div>


# Sort and use Two Pointer
	class Solution:
	    def threeSum(self, nums: List[int]) -> List[List[int]]:
		res = []
		nums.sort()					# [-1,0,1,2,-1,-4] -> [-4,-1,-1,0,1,2]
		for i, n in enumerate(nums):
		    if i > 0 and n == nums[i-1]:		# 第一个数 a_i 的 value 不重复
			continue

		    l, r = i + 1, len(nums) - 1			# 从 a_i 右侧第一位和 nums 最后一位开始 
		    while l < r:
			threeSum = n + nums[l] + nums[r]
			if threeSum > 0:			# 如果 sum 大于 0，则 right pointer 左移
			    r -= 1
			elif threeSum < 0:			# 如果 sum 小于 0，则 left pointer 右移
			    l += 1
			else:
			    res.append([n,nums[l],nums[r]])
			    l += 1 				# left pointer 右移，直至 l = r，从而得到对于 a_i 的所有组合
			    while nums[l] == nums[l - 1] and l < r:
				l += 1
		return res
