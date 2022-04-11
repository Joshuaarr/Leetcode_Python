# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = pin1 = ListNode()
        pin2 = ListNode()
        count = 0
        
        pin1.next = head
        pin2.next = head
        
        while count <= n:
            count += 1
            pin2 = pin2.next
        
        while pin2:
            pin2 = pin2.next
            pin1 = pin1.next
            
        pin1.next = pin1.next.next
        
        return dummy.next