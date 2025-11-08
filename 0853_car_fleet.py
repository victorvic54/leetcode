class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        print(time)
        for t in time[::-1]:
            if t > cur:
                res += 1
                cur = t
        return res

# Time: O(n log n)
# Space: O(n)

"""
pos: [0,5,3]
speed: [1,2,3]
time: [7.0, 1.33, 1.0]

pos: [10,8,0,5,3]
speed: [2,4,1,1,3]
time: [12.0, 3.0, 7.0, 1.0, 1.0]
"""
