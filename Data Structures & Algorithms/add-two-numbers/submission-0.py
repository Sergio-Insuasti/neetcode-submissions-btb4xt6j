# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        index = 0
        while l1:
            num1 += (10 ** index) * l1.val
            index += 1 
            l1 = l1.next

        num2 = 0
        index = 0
        while l2:
            num2 += (10 ** index) * l2.val
            index += 1 
            l2 = l2.next
        
        res = int(num1) + int(num2)

        if res == 0: return ListNode(0)

        dummy = ListNode(0)
        curr = dummy

        while res > 0:
            curr.next = ListNode(res % 10)
            curr = curr.next
            res //= 10

        return dummy.next
        