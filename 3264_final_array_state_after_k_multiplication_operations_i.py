class Number:
    def __init__(self, value, position):
        self.value = value
        self.position = position
    
    def __lt__(self, other):
        if self.value == other.value:
            return self.position < other.position
        return self.value < other.value

class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        sorted_nums = []
        for i in range(len(nums)):
            heapq.heappush(sorted_nums, Number(nums[i], i))
        
        for _ in range(k):
            number = heapq.heappop(sorted_nums)
            heapq.heappush(sorted_nums, Number(number.value * multiplier, number.position))
        
        output = nums.copy()
        for num in sorted_nums:
            output[num.position] = num.value
        return output


