# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        def mergeLists(list1, list2):
            if not list1: return list2
            if not list2: return list1
            

            d = node = ListNode()
        
            while list1 and list2:
                if list1.val < list2.val:
                    node.next = list1
                    list1 = list1.next
                else:
                    node.next = list2
                    list2 = list2.next
                node = node.next

            node.next = list1 or list2
            return d.next

        while len(lists) > 1:
            lists[0] = mergeLists(lists[0], lists[-1])
            lists = lists[:-1]
        return lists[0] if lists else None
