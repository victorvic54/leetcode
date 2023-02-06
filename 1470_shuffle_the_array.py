"""
For space complexity not equal O(1) is trivial.
The following solution is for space complexity equal O(1)
"""
class Solution:
    # Time complexity: O(n^2)
    def rotate(self, nums, start, end):
        length = (end - start + 1) // 2
        for i in range(length):
            nums[start+i], nums[end-i] = nums[end-i], nums[start+i]

    def shuffle(self, nums: List[int], n: int) -> List[int]:
        if n == 1:
            return nums

        self.rotate(nums, n, len(nums) - 2)
        for i in range(1, len(nums) - 2):
            self.rotate(nums, i, len(nums) - 2)
        return nums

class Solution:
    # Time complexity: O(n)
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n, len(nums)):
            nums[i] = (nums[i] * 1024) + nums[i-n]

        tmp = n
        for i in range(0, len(nums), 2):
            nums[i] = nums[tmp] % 1024
            nums[i+1] = nums[tmp] // 1024
            tmp += 1

        return nums

