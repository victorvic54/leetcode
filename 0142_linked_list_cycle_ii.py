"""
Let:
- x1 be the distance from start to start of loop
- x2 be the distance from start of loop to where slow and fast meet
- x3 be the distance where slow and fast meet to rest of the loop length (start of loop)

Distance travelled by slow, d(slow) = x1 + x2
Distance travelled by fast, d(fast) = x1 + x2 + x3 + x2
As fast travels twice as fast as slow, the relationship between the distances travelled by fast and slow pointers is,
= x1 + x2 + x3 + x2 = 2(x1 + x2)

Thus x1 = x3

So once the meeting point of fast and slow is found, if we reset any one pointer to head and let it move as much distance as the other would move from the meeting point, both pointers will meet at the start of the loop.
"""

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while (fast and fast.next):
            fast = fast.next.next
            slow = slow.next
            if (fast == slow):
                slow = head
                while (slow is not fast):
                    fast = fast.next
                    slow = slow.next
                return slow
        return None
