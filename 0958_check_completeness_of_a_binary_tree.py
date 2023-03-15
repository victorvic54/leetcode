# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#
class Solution:
    # better solution, check from child node
    def isCompleteTree(self, root: TreeNode) -> bool:
        # Check if the root node is None, if so, return True (an empty tree is complete)
        if not root:
            return True

        # Create a deque to store the nodes of the tree in level order
        q = deque([root])

        # Traverse the tree in level order
        while q[0] is not None:
            # Remove the first node from the deque
            node = q.popleft()
            # Add the left and right child nodes of the current node to the deque
            q.append(node.left)
            q.append(node.right)

        # Remove any remaining None nodes from the beginning of the deque
        while q and q[0] is None:
            q.popleft()

        # Check if there are any remaining nodes in the deque
        # If so, the tree is not complete, so return False
        # Otherwise, the tree is complete, so return True
        return not bool(q)


    # my ugly solution (check from parent node)
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        prev_expect_data = True

        while True:
            tmp_queue = deque()
            expect_data = True
            
            while queue:
                tmp_node = queue.popleft()
                if tmp_node.left:
                    if not expect_data or not prev_expect_data:
                        return False
                    tmp_queue.append(tmp_node.left)
                else:
                    expect_data = False
                
                if tmp_node.right:
                    if not expect_data or not prev_expect_data:
                        return False
                    tmp_queue.append(tmp_node.right)
                else:
                    expect_data = False

            if not tmp_queue:
                break

            prev_expect_data = expect_data
            queue.extend(tmp_queue)

        return True
