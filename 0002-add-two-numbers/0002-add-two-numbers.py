# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        upCnt = 0

        node1 = l1
        node2 = l2

        newList = ListNode(0)
        node3 = newList

        while node1 or node2 or upCnt:
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            
            tmp = val1 + val2 + upCnt
            upCnt = tmp//10
            tmp %= 10

            node3.next = ListNode(tmp)            
            node3 = node3.next

            node1 = node1.next if node1 else None
            node2 = node2.next if node2 else None

        return newList.next