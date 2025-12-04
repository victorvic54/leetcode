class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)

# Time: O(n)
# Space: O(k) where k = unique characters
