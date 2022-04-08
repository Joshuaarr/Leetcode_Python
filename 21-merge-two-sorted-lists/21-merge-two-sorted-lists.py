# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = cur = ListNode(0) #dummy和cur都指向列表头部
        if l1 == None or l2 == None:
            cur.next = l1 or l2
        
        while l1 and l2:    #判断l1,l2都非空，有一方是空的话就是none，则跳出循环
            if l1.val < l2.val:    #如果l1的首项小于l2首项
                cur.next = l1      #cur指向l1
                l1 = l1.next       #l1向后一位
            else:                  #如果l1的首项不小于l2首项
                cur.next = l2      
                l2 = l2.next       
            cur = cur.next         #cur向后移一位
            cur.next = l1 or l2    #六号位指向l1或l2（此时其中一个已经为空），剩下的非空与原结果连接
        return dummy.next          #dummy从一号位开始向外报