import collections
class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        d = deque()
        out = []
        for i, n in enumerate(nums):
            while d and nums[d[-1]] < n:
                d.pop()

            d.append(i)
            if d[0] == i - k:
                d.popleft()

            if i >= k-1:
                out.append(nums[d[0]])

        return out

"""
print(Solution().maxSlidingWindow([8,3,-1,-3,5,3,6,7], 3))

i = 0, curr element = 8, d = deque([]) and out = []
	 Added i to d
i = 1, curr element = 3, d = deque([0]) and out = []
	 Added i to d
i = 2, curr element = -1, d = deque([0, 1]) and out = []
	 Added i to d
	 Append nums[d[0]] = 8 to out
i = 3, curr element = -3, d = deque([0, 1, 2]) and out = [8]
	 Added i to d
	 Popped left from d because it's outside the window's leftmost (i-k)
	 Append nums[d[0]] = 3 to out
i = 4, curr element = 5, d = deque([1, 2, 3]) and out = [8, 3]
	 Popped from d because d has elements and nums[d.top] < curr element
	 Popped from d because d has elements and nums[d.top] < curr element
	 Popped from d because d has elements and nums[d.top] < curr element
	 Added i to d
	 Append nums[d[0]] = 5 to out
i = 5, curr element = 3, d = deque([4]) and out = [8, 3, 5]
	 Added i to d
	 Append nums[d[0]] = 5 to out
i = 6, curr element = 6, d = deque([4, 5]) and out = [8, 3, 5, 5]
	 Popped from d because d has elements and nums[d.top] < curr element
	 Popped from d because d has elements and nums[d.top] < curr element
	 Added i to d
	 Append nums[d[0]] = 6 to out
i = 7, curr element = 7, d = deque([6]) and out = [8, 3, 5, 5, 6]
	 Popped from d because d has elements and nums[d.top] < curr element
	 Added i to d
	 Append nums[d[0]] = 7 to out
[8, 3, 5, 5, 6, 7]

Time: O(n)
Space: O(n)
"""
