class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        ans = set()
        
        for t in triplets:
            if t[0] > target[0] or t[1] > target[1] or t[2] > target[2]:
                continue
            
            for i, v in enumerate(t):
                if v == target[i]:
                    ans.add(i)
        
        # Check if all three indices are present in the set
        return len(ans) == 3

"""
Time: O(n)
Space: O(1)
"""
