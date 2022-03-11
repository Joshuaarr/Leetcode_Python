<h2><a href="https://leetcode.com/problems/product-of-array-except-self/">238. Product of Array Except Self</a></h2><h3>Medium</h3><hr><div><p>Given an integer array <code>nums</code>, return <em>an array</em> <code>answer</code> <em>such that</em> <code>answer[i]</code> <em>is equal to the product of all the elements of</em> <code>nums</code> <em>except</em> <code>nums[i]</code>.</p>

<p>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</p>

<p>You must write an algorithm that runs in&nbsp;<code>O(n)</code>&nbsp;time and without using the division operation.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<pre><strong>Input:</strong> nums = [1,2,3,4]
<strong>Output:</strong> [24,12,8,6]
</pre><p><strong>Example 2:</strong></p>
<pre><strong>Input:</strong> nums = [-1,1,0,-3,3]
<strong>Output:</strong> [0,0,9,0,0]
</pre>
<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li><code>2 &lt;= nums.length &lt;= 10<sup>5</sup></code></li>
	<li><code>-30 &lt;= nums[i] &lt;= 30</code></li>
	<li>The product of any prefix or suffix of <code>nums</code> is <strong>guaranteed</strong> to fit in a <strong>32-bit</strong> integer.</li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong>&nbsp;Can you solve the problem in <code>O(1)&nbsp;</code>extra&nbsp;space complexity? (The output array <strong>does not</strong> count as extra space for space complexity analysis.)</p>
</div>

# 分情况，除法
	class Solution:
	    def productExceptSelf(self, nums: List[int]) -> List[int]:
		#分成有0和没0的情况，有两个及以上零输出0；只有一个零的除了零处以外输出零
		n = nums.count(0)
		if n == 0:
		    total = 1
		    for num in nums :
			total *= num
		    product = []
		    for i in range(len(nums)) :
			product.append(int(total/nums[i]))
		elif n > 1 :
		    n = len(nums)
		    product = [0]*n
		else :
		    m = len(nums)
		    product = [0]*m
		    i = 0
		    while i < m :
			if nums[i] == 0 :
			    product[i] = 1
			    j = 0
			    while j < m:
				if j != i :
				    product[i] *= nums[j]
				j += 1
			i += 1
		return product

# 储存从左到右的乘积
	class Solution:
	    def productExceptSelf(self, nums: List[int]) -> List[int]:
		prefix = 1 
		i = 0
		product = [1] * len(nums)
		
		while i < len(nums) :
		    product[i] = prefix
		    prefix = prefix * nums[i]
		    i += 1
		postfix = 1
		i = 1
		while i <= len(nums) :
		    product[-i] = product[-i] * postfix
		    postfix = postfix * nums[-i]
		    i += 1
		return(product)
		
当初始值为： ｜1｜2｜3｜4｜

第一轮输出为：	  	 ｜1 ｜1 ｜2｜6｜24｜

第二轮输出为：｜24｜24｜12｜4｜1｜

故结果为：      	 ｜24｜12｜8｜6｜



