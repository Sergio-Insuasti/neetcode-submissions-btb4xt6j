# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        def reverseList(head):
            if not head: return None
            if not head.next: return head

            prev, curr = None, head
            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev
        
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        for _ in range(left - 1):
            prev = prev.next

        subHead = prev.next
        subTail = subHead
        for _ in range(right-left):
            subTail = subTail.next
        
        nextNode = subTail.next
        subTail.next = None
        revList = reverseList(subHead)
        prev.next = revList
        subHead.next = nextNode

        return dummy.next
                

            

        
        