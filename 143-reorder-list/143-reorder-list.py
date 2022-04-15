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
            
        
        
       