"""
Given input: [1,2,3,4,5] and target: 6
Explanation:
For all subsequences starting with 1:
  with max = 5:  3 elements[2,3,4] can be picked up or not = 8 (2^3)
  with max = 4:  2 elements[2,3] can be picked up or not = 4 (2^2)
  with max = 3:  1 element[1] can be picked up or not = 2 (2^1)
  with max = 2:  0 elements[] can be picked up or not = 1 (2^0)
  with max = 1:  single element seq = 1
  total = 8+4+2+1+1 = 16 OR 2^((indexOf 5) - (indexOf 1)) = 2^(4-0) = 16

For all subsequences starting with 2:
  with max = 4:  1 elements[3] can be picked up or not = 2 (2^1)
  with max = 3:  0 element[] can be picked up or not = 1 (2^0)
  with max = 2:  single element seq = 1
  total = 2+1+1 = 4 OR 2^((indexOf 4) - (indexOf 2)) = 2^(4-2) = 4

For all subsequences starting with 3:
  with max = 3:  single element seq = 1
  total = 1 OR 2^((indexOf 3) - (indexOf 3)) = 2^(3-3) = 1

Total = 16+4+1 = 21
"""
class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        n, mod = len(nums), 10 ** 9 + 7
        nums.sort()
        
        answer = 0
        left, right = 0, n - 1

        while left <= right:
            if nums[left] + nums[right] <= target:
                answer = (answer + pow(2, right - left, mod)) % mod
                left += 1
            else:
                right -= 1
       
        return answer
