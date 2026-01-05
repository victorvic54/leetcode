class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        char_dict = Counter(s1)
        left = 0
        for right in range(len(s2)):
            if s2[right] in char_dict and char_dict[s2[right]] > 0:
                char_dict[s2[right]] -= 1
                if sum(char_dict.values()) == 0:
                    return True

                continue
            
            while s2[left] != s2[right]:
                char_dict[s2[left]] += 1
                left += 1
            
            left += 1
        
        return False

"""
n = len(s2)
m = len(s1)
k = 26 alphabets

Time: O(m + n * k)
Space: O(1)
"""
