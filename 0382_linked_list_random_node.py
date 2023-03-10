# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head
        self.num_list = self.getList()


    def getList(self):
        curr = self.head
        tmp_list = []

        while curr:
            tmp_list.append(curr.val)
            curr = curr.next

        return tmp_list


    def getRandom(self) -> int:
        return random.choice(self.num_list)


# reservoir sampling where it uses O(1) space
class Solution:
    def __init__(self, head: Optional[ListNode]):
        self.head = head


    def getRandom(self) -> int:
        res, n = 0, 0
        curr = self.head

        while curr:
            n += 1
            if random.randint(0, n - 1) == 0:
                res = curr.val
            
            curr = curr.next
        return res


# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

