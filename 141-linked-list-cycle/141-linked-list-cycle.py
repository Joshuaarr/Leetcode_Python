# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        pointer_1 = pointer_2 = head
        # 注意循环的判断：pointer_2 或 pointer_2 为 None 会报错
        while pointer_2 != None and pointer_2.next != None:
            pointer_1 = pointer_1.next
            pointer_2 = pointer_2.next.next
            if pointer_1 == pointer_2:
                return True
        return False