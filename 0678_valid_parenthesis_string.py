class Solution:
    def checkValidString(self, s: str) -> bool:
        leftMin, leftMax = 0, 0

        for c in s:
            if c == "(":
                leftMin, leftMax = leftMin + 1, leftMax + 1
            elif c == ")":
                leftMin, leftMax = leftMin - 1, leftMax - 1
            else:
                leftMin, leftMax = leftMin - 1, leftMax + 1
            if leftMax < 0:
                return False
            if leftMin < 0:
                leftMin = 0
        return leftMin == 0

"""
s = "(*)"

char  leftMin	leftMax	 Note
(	  1	        1	     one open
*	  0	        2	     could close or open
)	  -1 → 0    1	     one closed; clamp leftMin = 0

Time: O(n)
Space: O(1)
"""
