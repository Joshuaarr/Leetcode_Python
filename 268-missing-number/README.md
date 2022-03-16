<h2><a href="https://leetcode.com/problems/missing-number/">268. Missing Number</a></h2><h3>Easy</h3><hr><div><p>Given an array <code>nums</code> containing <code>n</code> distinct numbers in the range <code>[0, n]</code>, return <em>the only number in the range that is missing from the array.</em></p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>

<pre><strong>Input:</strong> nums = [3,0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong>Example 2:</strong></p>

<pre><strong>Input:</strong> nums = [0,1]
<strong>Output:</strong> 2
<strong>Explanation:</strong> n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> nums = [9,6,4,2,3,5,7,0,1]
<strong>Output:</strong> 8
<strong>Explanation:</strong> n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>n == nums.length</code></li>
	<li><code>1 &lt;= n &lt;= 10<sup>4</sup></code></li>
	<li><code>0 &lt;= nums[i] &lt;= n</code></li>
	<li>All the numbers of <code>nums</code> are <strong>unique</strong>.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> Could you implement a solution using only <code>O(1)</code> extra space complexity and <code>O(n)</code> runtime complexity?</p>
</div>

# Brute Force
	class Solution:
	    def missingNumber(self, nums: List[int]) -> int:
		for num in range(len(nums) + 1):
		    if num not in nums:
			return num
			
# See which number is missing
	class Solution:
	    def missingNumber(self, nums: List[int]) -> int:
		n = len(nums)
		return int(n * (n + 1) * 0.5) - sum(nums)
		
# Quicker Way
	class Solution:
	    def missingNumber(self, nums: List[int]) -> int:
		res = len(nums)			# res 初始值设为 nums 的长度 n
		for i in range(len(nums)): 	# 这里相当于对 0 到 n - 1 进行求和，同时减去 sum(nums)
		    res += (i - nums[i])	# 因此需要将 res 初始值设为 n
		return res
# Binary Solution
	class Solution:
	    def missingNumber(self, nums: List[int]) -> int:
		res = len(nums)
		for i in range(len(nums)):
		    res ^= nums[i] ^ i
		return res
Using the XOR(the exclusive OR operator): 
	(1,1) or (0,0) -> 0
	(1,0) or (0,1) -> 1
	
For example,

	(5 ^ 5) = (1 0 1)^(1 0 1) = (0 0 0) = 0
	
and the order of numbers doesn't matter,

	(5 ^ 3 ^ 5) = (5 ^ 5 ^ 3) = 3
	
	
