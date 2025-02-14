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
            tmp = upCnt
            
            if node1:
                tmp += node1.val
                node1 = node1.next
            if node2:
                tmp += node2.val
                node2 = node2.next
            
            upCnt = tmp//10
            tmp %= 10

            node3.next = ListNode(tmp)            
            node3 = node3.next

        return newList.next