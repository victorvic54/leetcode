# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.kth_smallest = 0
        self.n_left = k
        def backtracking(node):
            if node == None:
                return
            
            backtracking(node.left)
            self.n_left -= 1
            if self.n_left == 0:
                self.kth_smallest = node.val
            backtracking(node.right)
            return
        backtracking(root)
        return self.kth_smallest


# N = number of nodes
# Time: O(N) where k = N, average = O(H + k)
# Space: O(N) (skewed)
#        O(log N) (balanced)
