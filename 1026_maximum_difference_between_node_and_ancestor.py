# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def traverse(root):
            if root.left == None and root.right == None:
                return root.val, root.val, 0

            min_val = root.val
            max_val = root.val
            max_diff = 0
            if root.left != None:
                min_val_left, max_val_left, max_diff_left = traverse(root.left)
                min_val = min(min_val, min_val_left)
                max_val = max(max_val, max_val_left)
                max_diff = max(max_diff, max_diff_left, abs(root.val - min_val_left), abs(root.val - max_val_left))

            if root.right != None:
                min_val_right, max_val_right, max_diff_right = traverse(root.right)
                min_val = min(min_val, min_val_right)
                max_val = max(max_val, max_val_right)
                max_diff = max(max_diff, max_diff_right, abs(root.val - min_val_right), abs(root.val - max_val_right))

            return min_val, max_val, max_diff
        
        _, _, max_diff = traverse(root)
        return max_diff

