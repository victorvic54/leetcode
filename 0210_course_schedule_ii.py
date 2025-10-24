class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # kahn algorithm
        adj_list = defaultdict(list)
        indeg = [0] * numCourses
        for a, b in prerequisites:
            # edge [a, b] means: to take course a, you must have taken b => [b -> a]
            adj_list[b].append(a)
            indeg[a] += 1
        
        q = deque([])
        for i in range(len(indeg)):
            if indeg[i] == 0:
                q.append(i)
        
        courses = []
        while q:
            u = q.popleft()
            courses.append(u)
            for v in adj_list[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        if len(courses) != numCourses:
            return []

        return courses

# Time: O(V + E)
# Space: O(V + E)
