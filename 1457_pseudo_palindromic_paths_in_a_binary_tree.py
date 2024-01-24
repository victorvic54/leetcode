# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def backtracking(node, state):
            if node.left == None and node.right == None:
                if state.bit_count() > 2:
                    return 0
                else:
                    return 1
            
            total = 0
            if node.left:
                left_state = state ^ (1 << (ord(str(node.left.val)) - ord('1')))
                total += backtracking(node.left, left_state)
            
            if node.right:
                right_state = state ^ (1 << (ord(str(node.right.val)) - ord('1')))
                total += backtracking(node.right, right_state)
            
            return total

        init_state = 1 << 9 ^ (1 << (ord(str(root.val)) - ord('1')))
        return backtracking(root, init_state)
