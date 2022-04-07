<h2><a href="https://leetcode.com/problems/reverse-linked-list/">206. Reverse Linked List</a></h2><h3>Easy</h3><hr><div><p>Given the <code>head</code> of a singly linked list, reverse the list, and return <em>the reversed list</em>.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex1.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [5,4,3,2,1]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/02/19/rev1ex2.jpg" style="width: 182px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2]
<strong>Output:</strong> [2,1]
</pre>

<p><strong>Example 3:</strong></p>

<pre><strong>Input:</strong> head = []
<strong>Output:</strong> []
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is the range <code>[0, 5000]</code>.</li>
	<li><code>-5000 &lt;= Node.val &lt;= 5000</code></li>
</ul>

<p>&nbsp;</p>
<p><strong>Follow up:</strong> A linked list can be reversed either iteratively or recursively. Could you implement both?</p>
</div>

# Iteration（迭代） T: O(n); M: O(1)

	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, val=0, next=None):
	#         self.val = val
	#         self.next = next
	class Solution:
	    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		'''
		iteration（迭代） T: O(n); M: O(1)

		Null  ->  (1)  ->  (2)  ->  (3)
		prev  ->  curr -> curr.next
		prev=(1)->Null -> curr -> cur.next

		''' 
		prev = None
		curr = head

		while curr: # While curr is not Null
		    nxt = curr.next #save cur.next with a pointer first
		    curr.next = prev
		    prev = curr
		    curr = nxt
		return prev

# recursion（递归） T: O(n); M: O(n)
	class Solution:
	    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
		'''
		recursion（递归） T: O(n); M: O(n)

		To breakdown into sub-problems
		0. sub-sub-problem: (3)   ->   Null
		   Do nothing
		1. sub-problem: (2)   ->   (3)   ->
		   (3)   ->   (2) and (2)   ->   Null 
		   (3)   ->   (2)   ->   Null   
		2. whole thing: (1)   ->   (2)   ->   (3)   ->
		   (2)   ->   (1) and (1)   ->   Null 
		   (3)   ->   (2)   ->   (1)   ->   Null
		''' 
		# base case: if head = null, return none
		if not head:
		    return None

		newHead = head
		if head.next: # if head.next is not null
		    newHead = self.reverseList(head.next)
		    head.next.next = head
		head.next = None

		return newHead
		
![IMG_069029CDE1BD-1](https://user-images.githubusercontent.com/48045950/162167856-0dc1e916-4ee2-4f88-8b06-bb35f87e88b2.jpeg)
