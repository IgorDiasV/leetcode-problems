# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        nodes = []
        while head:
            nodes.append(head)
            if head.next in nodes:
                return True
            head = head.next
        return False
    
