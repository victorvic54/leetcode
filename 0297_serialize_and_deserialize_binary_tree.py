class Codec:
    def serialize(self, root):
        vals = []
        def dfs(node):
            if not node:
                vals.append(None)
                return
            vals.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return json.dumps(vals)

    def deserialize(self, data):
        vals = deque(json.loads(data))
        def dfs():
            val = vals.popleft()
            if val is None:
                return None
            node = TreeNode(val)
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()


# N = number of nodes
# Time: O(N)
# Space: O(N) + O(H) = O(N)
