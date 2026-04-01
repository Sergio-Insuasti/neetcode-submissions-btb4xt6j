# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        def getKth(curr, k):
            while curr and k > 0:
                curr = curr.next
                k -= 1
            return curr
        d = ListNode(0, head)
        # the one note before the kth group
        groupPrev = d

        while True:
            # find kth node
            kth = getKth(groupPrev, k)
            # not kth means the final group too small
            # break and return
            if not kth:
                break
            groupNext = kth.next
            # Reverse k group
            prev, curr = kth.next, groupPrev.next
            while curr != groupNext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            # reassign pointers to first node of group
            # and last node of group for future ref
            temp = groupPrev.next
            groupPrev.next = kth
            groupPrev = temp
        return d.next

            

