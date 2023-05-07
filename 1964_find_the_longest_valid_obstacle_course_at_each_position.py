"""
Example
obstacles = [1,4,5,2,3]

Step #1:
Insert ob[0] to ls, the inserting index is 0. Append ob[0] to ls and update answer[0] = 0 + 1 = 1
Value of ls currently: [1]

Step #2:
Insert ob[1] = 4 to ls, the inserting index is 1. Append 4 to ls and update answer[1] = 1 + 1 = 2
Value of ls currently: [1, 4]

Step #3:
Insert ob[2] = 5 to ls, the inserting index is 2. Append 5 to ls and update answer[1] = 1 + 2 = 3
Value of ls currently: [1, 4, 5]

Step #4:
Insert ob[3] = 2 to ls, the inserting index is 1. Update ls[1] = 2 and update answer[3] = 1 + 1 = 2
Value of ls currently: [1, 2, 5]

Step #5:
Insert ob[4] = 3 to ls, the inserting index is 2. Update ls[2] = 3 and update answer[4] = 1 + 2 = 3
Value of ls currently: [1, 2, 3]
"""
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        n = len(obstacles)
        answer = [1] * n
        
        # ls[i] records the lowest increasing sequence of length i + 1.
        ls = []
    
        for i, height in enumerate(obstacles):
            # Find the rightmost insertion position idx (work only for sorted list).
            idx = bisect.bisect_right(ls, height)
            
            if idx == len(ls):
                ls.append(height)
            else: 
                ls[idx] = height
            answer[i] = idx + 1
            
        return answer

