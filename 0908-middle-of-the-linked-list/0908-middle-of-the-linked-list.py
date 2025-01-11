# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        lenList = 0
        current1 = head

        while current1:
            lenList += 1
            current1 = current1.next
        
        current2 = head
        n = lenList // 2

        for _ in range(n):
            current2 = current2.next

        ans = ListNode(current2.val)
        current_ans = ans
        current2 = current2.next
        
        while current2:
            new_node = ListNode(current2.val)
            current_ans.next = new_node
            current_ans = new_node
            current2 = current2.next

        return ans