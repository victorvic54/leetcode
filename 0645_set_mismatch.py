class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        ans = []
        initial_set = set()
        for i in range(1, len(nums) + 1):
            initial_set.add(i)
        
        for num in nums:
            if num in initial_set:
                initial_set.remove(num)
            else:
                ans.append(num)
        
        return ans + list(initial_set)

