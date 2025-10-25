from collections import defaultdict, deque
from typing import List

class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        # Collect all unique chars
        chars = set()
        for w in words:
            chars |= set(w)

        adj = defaultdict(set)
        indeg = defaultdict(int)

        # Build edges by first differing character; check invalid prefix
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            # invalid: longer word comes before its prefix
            if len(w1) > len(w2) and w1.startswith(w2):
                return ""
            # add first difference edge
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    if w2[j] not in adj[w1[j]]:
                        adj[w1[j]].add(w2[j])
                        indeg[w2[j]] += 1
                    break

        # Kahn's algorithm
        q = deque([c for c in chars if indeg[c] == 0])
        order = []
        print(q, indeg, adj, chars)
        while q:
            u = q.popleft()
            order.append(u)
            for v in adj[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # If not all chars were output, there is a cycle / contradiction
        return "" if len(order) != len(chars) else "".join(order)
    
"""
Time complexity:
| Step                      | Work             | Description                            |
| ------------------------- | ---------------- | -------------------------------------- |
| Collect unique characters | O(T)             | Iterate over every letter              |
| Build precedence edges    | O(T + E)         | Compare adjacent words and build edges |
| Topological sort          | O(V + E)         | Each node and edge visited once        |
| **Total**                 | **O(T + V + E)** | Summing all terms                      |

Space complexity:
| Component         | Space        | Description                         |
| ----------------- | ------------ | ----------------------------------- |
| Adjacency list    | O(E)         | Stores outgoing edges per character |
| Indegree map      | O(V)         | One integer per character           |
| Queue             | O(V)         | Nodes with indegree 0               |
| Set of characters | O(V)         | All unique chars                    |
| **Total**         | **O(V + E)** |                                     |
"""

