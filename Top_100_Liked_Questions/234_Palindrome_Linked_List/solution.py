# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        values = []
        while head:
            values.append(head.val)
            head = head.next
        if(len(values)%2!=0):
            half = len(values)//2
            values.pop(half)
        half = len(values)//2
        return values[:half] == values[:half-1:-1]