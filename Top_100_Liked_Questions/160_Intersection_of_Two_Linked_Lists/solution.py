# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        list_values = []
        startA, startB = headA, headB
        while headA:
            list_values.append(headA)
            headA = headA.next
        while headB:
            if headB in list_values:
                return headB
            headB = headB.next
        return None