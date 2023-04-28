class Solution:
    def numSimilarGroups(self, strs: List[str]) -> int:
        edge_list = defaultdict(list)
        strs_len = len(strs[0])

        for i in range(len(strs) - 1):
            for j in range(i + 1, len(strs)):
                diff = 0
                for k in range(strs_len):
                    if strs[i][k] != strs[j][k]:
                        diff += 1

                if diff <= 2:
                    edge_list[i].append(j)
                    edge_list[j].append(i)

        queue = deque([])
        visited = set()
        total_group = 0
        for i in range(len(strs)):
            if i in visited:
                continue

            total_group += 1
            queue.extend(edge_list[i])
            while queue:
                node = queue.popleft()
                if node in visited:
                    continue

                visited.add(node)
                queue.extend(edge_list[node])
        
        return total_group

