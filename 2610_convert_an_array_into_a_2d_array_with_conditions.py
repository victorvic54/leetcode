class Solution:
    def findMatrix(self, nums: List[int]) -> List[List[int]]:
        num_map = defaultdict(int)
        max_counter = 0
        for num in nums:
            num_map[num] += 1
            max_counter = max(max_counter, num_map[num])

        ans = [[] for i in range(max_counter)]
        for key in num_map:
            for i in range(num_map[key]):
                ans[i].append(key)

        return ans
