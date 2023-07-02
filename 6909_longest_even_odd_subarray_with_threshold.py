class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:
        result = 0
        
        for i in range(len(nums)):
            if nums[i] % 2 != 0:
                continue

            j = 0
            for j in range(i, len(nums)):
                if nums[j] > threshold:
                    j -= 1
                    break

                if j == len(nums) - 1:
                    break
                
                if nums[j] % 2 == nums[j + 1] % 2:
                    break
                
            
            result = max(result, j - i + 1)
                
        return result
