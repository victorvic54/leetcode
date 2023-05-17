# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
# O(n) space
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        arr = []

        while head:
            arr.append(head.val)
            head = head.next
        
        mid = len(arr) // 2
        return max([sum(x) for x in zip(arr[:mid], arr[mid:][::-1])])


# O(1) space
class Solution(object):
    def pairSum(self, head):
        slow, fast = head, head
        maximumSum = 0

        # Get middle of the linked list.
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse second half of the linked list.
        curr, prev = slow, None
        while curr:       
            curr.next, prev, curr = prev, curr, curr.next
        
        start = head
        while prev:
            maximumSum = max(maximumSum, start.val + prev.val)
            prev = prev.next
            start = start.next

        return maximumSum

