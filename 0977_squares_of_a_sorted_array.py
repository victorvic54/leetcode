class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left_ptr = None
        right_ptr = None
        for i in range(1, len(nums)):
            if nums[i-1] < 0 and nums[i] >= 0:
                left_ptr = i - 1
                right_ptr = i
        
        if left_ptr == None or right_ptr == None:
            if nums[0] < 0:
                left_ptr = len(nums) - 1
            if nums[0] >= 0:
                right_ptr = 0
        
        ans = []
        while True:
            if (left_ptr != None and left_ptr >= 0) and (right_ptr != None and right_ptr < len(nums)):
                if abs(nums[left_ptr]) < abs(nums[right_ptr]):
                    ans.append(nums[left_ptr] * nums[left_ptr])
                    left_ptr -= 1
                else:
                    ans.append(nums[right_ptr] * nums[right_ptr])
                    right_ptr += 1
            elif (left_ptr != None and left_ptr >= 0):
                ans.append(nums[left_ptr] * nums[left_ptr])
                left_ptr -= 1
            elif (right_ptr != None and right_ptr < len(nums)):
                ans.append(nums[right_ptr] * nums[right_ptr])
                right_ptr += 1
            else:
                break

        return ans

