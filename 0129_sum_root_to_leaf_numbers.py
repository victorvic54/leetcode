# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.total = 0
        self.helper("", root)
        return self.total

    def helper(self, prev_val, node):
        prev_val += str(node.val)

        if node.left and node.right:
            self.helper(prev_val, node.left)
            self.helper(prev_val, node.right)
        elif node.left:
            self.helper(prev_val, node.left)
        elif node.right:
            self.helper(prev_val, node.right)
        else:
            self.total += int(prev_val)

