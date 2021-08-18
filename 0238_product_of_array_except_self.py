class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_arr = [None] * len(nums)
        right_arr = [None] * len(nums)
        answer = [None] * len(nums)
        
        left_arr[0] = 1
        right_arr[-1] = 1
        
        for i in range(1, len(nums)):
            left_arr[i] = left_arr[i-1] * nums[i-1]
            
        for i in range(len(nums)-2, -1, -1):
            right_arr[i] = right_arr[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            answer[i] = left_arr[i] * right_arr[i]
            
        return answer