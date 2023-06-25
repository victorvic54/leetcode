class Solution:
    def countBeautifulPairs(self, nums: List[int]) -> int:
        result = 0
        
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                first = int(str(nums[i])[0])
                second = int(str(nums[j])[-1])
                tmp_result = gcd(first, second)
                    
                if tmp_result == 1:
                    result += 1
        return result
