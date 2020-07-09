# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    
    ###########################
    # Using recursion         #
    ###########################
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        result = head.next;
        tmp = head.next.next;
        
        result.next = head;
        head.next = self.swapPairs(tmp);
        
        return result;

    
    ###########################
    # Using 2 nodes           #
    ###########################
    
    def swapPairs(self, head: ListNode) -> ListNode:
        if not (head and head.next):
            return head
        
        result = head.next
        
        while (head and head.next):
            tmp = head.next.next
            head.next.next = head
            head = head.next
            
            if (tmp and tmp.next):
                head.next.next = tmp.next
            else:
                head.next.next = tmp

            head = tmp
            
        return result
    
    
    
    ###########################
    # Using 3 nodes           #
    #                         #
    # pre -> a -> b -> b.next #
    ###########################
    
    def swapPairs(self, head):
        pre, pre.next = self, head
        
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next
            pre = a

        return self.next