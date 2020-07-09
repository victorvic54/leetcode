# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, listnode1, listnode2):
        if (not listnode1):
            return listnode2
        elif (not listnode2):
            return listnode1
        else:
            if (listnode1.val <= listnode2.val):
                listnode1.next = self.mergeTwoLists(listnode1.next, listnode2)
                return listnode1
            else:
                listnode2.next = self.mergeTwoLists(listnode1, listnode2.next)
                return listnode2
        
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        low = 0
        hi = len(lists)
        
        if (hi == 0):
            return None
        elif (hi == 1):
            return lists[0]
        elif (hi == 2):
            return self.mergeTwoLists(lists[0], lists[1])
        else:
            mid = (low + hi) // 2
            return self.mergeTwoLists(
                self.mergeKLists(lists[0:mid]),
                self.mergeKLists(lists[mid:])
            )
        
        
##############################################################################
from Queue import PriorityQueue

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = ListNode(None)
        curr = dummy
        q = PriorityQueue()
        
        for node in lists:
            if node:
                q.put((node.val,node))
        
        while q.qsize() > 0:
            curr.next = q.get()[1]
            curr=curr.next
            if curr.next:
                q.put((curr.next.val, curr.next))
        
        return dummy.next