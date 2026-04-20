# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head: return head

        curr = head
        while curr.next:
            gcd = math.gcd(curr.val, curr.next.val)
            g_node = ListNode(gcd)
            g_node.next = curr.next
            curr.next = g_node
            curr = g_node.next
        return head
            
        