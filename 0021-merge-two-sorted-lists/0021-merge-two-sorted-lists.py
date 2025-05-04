# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        newList = []

        if list1:
            node1 = list1
            
            while node1:
                newList.append(node1.val)
                node1 = node1.next
        
        if list2:
            node2 = list2

            while node2:
                newList.append(node2.val)
                node2 = node2.next

        if newList:
            dummy = ListNode(0)
            ans = dummy

            for n in sorted(newList):
                ans.next = ListNode(n)
                ans = ans.next

            return dummy.next