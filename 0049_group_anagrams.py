class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:    
        ans = defaultdict(list)

        for s in strs:
            key = "".join(sorted(s))
            ans[key].append(s)
        
        return list(ans.values())

"""
n = number of strings
k = maximum string length
Time: O(n · k log k) total
Space: O(n · k)
"""

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = defaultdict(list)

        for s in strs:
            # key is a tuple of 26 counts (assuming lowercase letters)
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            ans[tuple(count)].append(s)

        return list(ans.values())

# Time: O(n · k)
# Space: O(n · k)
