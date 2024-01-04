class Solution:
    def minOperations(self, nums: List[int]) -> int:
        num_dict = defaultdict(int)
        for num in nums:
            num_dict[num] += 1

        ans = 0
        for key in num_dict:
            if num_dict[key] == 1:
                return -1
            
            if num_dict[key] % 3 == 0:
                ans += num_dict[key] // 3
            else:
                ans += (num_dict[key] // 3) + 1
                
        return ans
