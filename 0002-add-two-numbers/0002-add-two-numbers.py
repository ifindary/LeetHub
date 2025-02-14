# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        upCnt = 0
        node1 = l1
        node2 = l2

        newList = ListNode(0)
        node3 = newList

        while node1 or node2 or upCnt:
            if node1 and node2:
                tmp = node1.val + node2.val + upCnt
                node1 = node1.next
                node2 = node2.next
            elif node1:
                tmp = node1.val + upCnt
                node1 = node1.next
            elif node2:
                tmp = node2.val + upCnt
                node2 = node2.next
            else:
                tmp = upCnt
            
            if tmp >= 10:
                upCnt = 1
                tmp -= 10
            else:
                upCnt = 0

            node3.next = ListNode(tmp)            
            node3 = node3.next

        return newList.next