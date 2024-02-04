class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = -float('inf')
        total_sum = 0
        
        num_dict = {}
        for num in nums:
            if num not in num_dict:
                num_dict[num] = total_sum
            else:
                num_dict[num] = min(num_dict[num], total_sum)
                
            total_sum += num
            if num - k in num_dict:
                ans = max(ans, total_sum - num_dict[num-k])
            if num + k in num_dict:
                ans = max(ans, total_sum - num_dict[num+k])
            
        return ans if ans != -float('inf') else 0

