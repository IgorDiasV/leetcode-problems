# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        number_one = []
        number_two = []

        sum1 = 0
        sum2 = 0
        mult1 = 1
        mult2 = 1
        while l1 or l2:
            if l1:
                sum1 += l1.val * mult1
                mult1 *= 10
                l1 = l1.next
            if l2:
                sum2 += l2.val * mult2
                mult2 *= 10
                l2 = l2.next

        sum_list = ListNode()
        head = sum_list
        list_values = str(sum1 + sum2)[::-1]
        size_list = len(list_values)
        for i in range(size_list):
            sum_list.val = int(list_values[i])
            if( i < size_list -1):
                sum_list.next = ListNode()
                sum_list = sum_list.next
        return head
