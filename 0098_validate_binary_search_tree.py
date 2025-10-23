# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # Two-pass straight forward in order traversal
    def isValidBST(self, root: TreeNode) -> bool:
        result = []
        
        def inorder_traversal(node):
            if (not node):
                return
            
            inorder_traversal(node.left)
            result.append(node.val)
            inorder_traversal(node.right)
            
        inorder_traversal(root)
        
        for i in range(1, len(result)):
            if (result[i-1] >= result[i]):
                return False
            
        return True

    # Time: O(N)
    # Space: O(N) for skewed, O(log N) for balanced tree
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def backtracking(node, prev_node_range):
            if node == None:
                return True
            
            if node.left:
                if node.left.val >= node.val:
                    return False
                if prev_node_range and not (prev_node_range[0] < node.left.val < prev_node_range[1]):
                    return False

            if node.right:
                if node.right.val <= node.val:
                    return False
                if prev_node_range and not (prev_node_range[0] < node.right.val < prev_node_range[1]):
                    return False
            
            return backtracking(node.left, [prev_node_range[0], min(prev_node_range[1], node.val)]) and \
                backtracking(node.right, [max(prev_node_range[0], node.val), prev_node_range[1]])

        return backtracking(root, [-float('inf'), float('inf')])


    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, low, high):
            if not node:
                return True
            if not (low < node.val < high):
                return False
            return dfs(node.left, low, node.val) and dfs(node.right, node.val, high)
        return dfs(root, float("-inf"), float("inf"))


    # One pass in order traversal
    # Since we know in order traversal result a sorted array, and res is the one that
    # contain the last visited node value, it should be smaller than the next visited node val
    def isValidBST(self, root: TreeNode) -> bool:
        stack, res = [], []
        
        while True:
            while root:
                stack.append(root)
                root = root.left
            
            if not stack:
                return True
            
            node = stack.pop()
            # res stores the current values in in-order traversal order,
            # node.val should larger than the last element in res
            if res and node.val <= res[-1]:
                return False
            
            res.append(node.val)
            root = node.right
