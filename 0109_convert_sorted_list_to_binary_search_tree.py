# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        self.data_ls = []
        while head:
            self.data_ls.append(head.val)
            head = head.next
        return self.make_treenode(0, len(self.data_ls) - 1)

    def make_treenode(self, left, right):
        if left <= right:
            mid = (left + right) // 2
            n = TreeNode(self.data_ls[mid])
            n.left  = self.make_treenode(left, mid - 1)
            n.right = self.make_treenode(mid + 1, right)
            return n

