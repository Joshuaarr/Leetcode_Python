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