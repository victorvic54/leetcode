# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        if (n < 1):
            return []

        def generate_trees(low, high):
            ans = []
            
            if (low > high):
                return [None]

            for root in range(low, high + 1):
                left_subtree = generate_trees(low, root - 1)        # small number go to the left
                right_subtree = generate_trees(root + 1, high)      # big number go to the right

                for left in left_subtree:
                    for right in right_subtree:
                        tree_root = TreeNode(root)
                        tree_root.left = left
                        tree_root.right = right
                        ans.append(tree_root)

            return ans

        return generate_trees(1, n)