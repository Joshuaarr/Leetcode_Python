<h2><a href="https://leetcode.com/problems/reorder-list/">143. Reorder List</a></h2><h3>Medium</h3><hr><div><p>You are given the head of a singly linked-list. The list can be represented as:</p>

<pre>L<sub>0</sub> → L<sub>1</sub> → … → L<sub>n - 1</sub> → L<sub>n</sub>
</pre>

<p><em>Reorder the list to be on the following form:</em></p>

<pre>L<sub>0</sub> → L<sub>n</sub> → L<sub>1</sub> → L<sub>n - 1</sub> → L<sub>2</sub> → L<sub>n - 2</sub> → …
</pre>

<p>You may not modify the values in the list's nodes. Only nodes themselves may be changed.</p>

<p>&nbsp;</p>
<p><strong>Example 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/04/reorder1linked-list.jpg" style="width: 422px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4]
<strong>Output:</strong> [1,4,2,3]
</pre>

<p><strong>Example 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/09/reorder2-linked-list.jpg" style="width: 542px; height: 222px;">
<pre><strong>Input:</strong> head = [1,2,3,4,5]
<strong>Output:</strong> [1,5,2,4,3]
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The number of nodes in the list is in the range <code>[1, 5 * 10<sup>4</sup>]</code>.</li>
	<li><code>1 &lt;= Node.val &lt;= 1000</code></li>
</ul>
</div>


# Brute force
	# Definition for singly-linked list.
	# class ListNode:
	#     def __init__(self, val=0, next=None):
	#         self.val = val
	#         self.next = next
	class Solution:
	    def reorderList(self, head: Optional[ListNode]) -> None:
		"""
		Do not return anything, modify head in-place instead.
		"""

		# find the middle point
		slow, fast = head, head
		while fast.next and fast.next.next:
		    slow = slow.next
		    fast = fast.next.next

		# reverse the second half of the list
		prev, curr = None, slow.next
		slow.next = None     # mind this step!
		while curr:
		    temp = curr.next
		    curr.next = prev
		    prev = curr
		    curr = temp


		# insert the second half to the first half
		head1, head2 = head, prev
		while head2:
		    temp = head1.next
		    head1.next = head2
		    head1 = head2
		    head2 = temp
            
        
        
       
