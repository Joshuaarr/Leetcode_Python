<h2><a href="https://leetcode.com/problems/contains-duplicate/">217. Contains Duplicate</a></h2><h3>Easy</h3><hr><div><p>Given an integer array <code>nums</code>, return <code>true</code> if any value appears <strong>at least twice</strong> in the array, and return <code>false</code> if every element is distinct.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,1]
<strong>Output:</strong> true
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> false
</pre><p><strong>Example 3:</strong></p>
<pre><strong>Input:</strong> nums = [1,1,1,3,3,4,3,2,4,2]
<strong>Output:</strong> true
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>1 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-10<sup>9</sup> &lt;= nums[i] &lt;= 10<sup>9</sup></code></li>
</ul>
</div>

# Brute Force （TLE）
	class Solution:
	    def containsDuplicate(self, nums: List[int]) -> bool:
		l = len(nums)
		i = 0
		while i < l :
		    if nums[i] in nums[i+1::] :
			return True
		    else :
			i += 1
		return False
# Use List to Track（TLE）
	class Solution:
	    def containsDuplicate(self, nums: List[int]) -> bool:
		m = []
		for num in nums :
		    if num in m :
			return True
		    else :
			m.append(num)
		return False
# Use Set to Track （admitted）



* 对于几种python数据解构的解释：https://medium.com/kung-%E7%9A%84%E6%97%A5%E5%B8%B8/python-%E5%AD%B8%E7%BF%92%E7%AD%86%E8%A8%98-006-%E5%BA%8F%E5%B0%8D-tuple-%E9%9B%86%E5%90%88-set-%E8%88%87%E5%AD%97%E5%85%B8-dict-33186c42049c *
# Samrt Cheated Way with Set（admitted）
	class Solution:
	    def containsDuplicate(self, nums: List[int]) -> bool:
		return len(nums) > len(set(nums))
