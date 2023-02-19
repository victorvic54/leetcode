# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = collections.deque([root])
        even_level = False

        while queue:
            tmp_result = collections.deque()

            for _ in range(len(queue)):
                node = queue.popleft()
                if even_level:
                    tmp_result.appendleft(node.val)
                else:
                    tmp_result.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            result.append(list(tmp_result))
            even_level = not even_level

        return result
