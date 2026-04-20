# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        left = head
        right = head.next

        while right:
            gcd = ListNode(val = math.gcd(left.val, right.val))
            left.next = gcd
            gcd.next = right
            left = right
            right = right.next
        return head
            
        