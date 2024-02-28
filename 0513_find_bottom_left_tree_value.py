# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        def traverse(root, height):
            if root.left == None and root.right == None:
                return root.val, height
            elif root.left == None:
                return traverse(root.right, height + 1)
            elif root.right == None:
                return traverse(root.left, height + 1)
            else:
                left_val, left_height = traverse(root.left, height + 1)
                right_val, right_height = traverse(root.right, height + 1)
                if left_height >= right_height:
                    return left_val, left_height
                else:
                    return right_val, right_height

        val, height = traverse(root, 0)
        return val
