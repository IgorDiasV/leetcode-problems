# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        reverseListValues = ListNode()
        listvalues = []
        while head:
            listvalues.append(head)
            head = head.next
        head = reverseListValues
        for node in listvalues[::-1]:
            reverseListValues.next = node
            reverseListValues = reverseListValues.next
        reverseListValues.next = None
        return head.next