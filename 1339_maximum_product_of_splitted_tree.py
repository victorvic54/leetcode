# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.MOD = 10**9 + 7

    def is_greater_than(self, num, divisor, remainder):
        if (divisor * self.MOD) + remainder < num:
            return True
        return False

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_divisor = 0
        self.max_remainder = 0
        sum_all_nodes = self.sum_all_nodes(root)
        
        def backtrack(node):
            if not node:
                return 0
            
            left_total = backtrack(node.left)
            right_total = backtrack(node.right)
            total = node.val + left_total + right_total
            tmp_num = total * (sum_all_nodes - total)
            if self.is_greater_than(tmp_num, self.max_divisor, self.max_remainder):
                self.max_divisor = tmp_num // self.MOD
                self.max_remainder = tmp_num % self.MOD

            return total
        
        backtrack(root)
        return self.max_remainder

    def sum_all_nodes(self, root):
        if not root:
            return 0        
        return root.val + self.sum_all_nodes(root.left) + self.sum_all_nodes(root.right)

# Time: O(n)
# Space: O(h)
