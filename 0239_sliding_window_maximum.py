class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        index_queue = []
        result = []
        
        for i in range(len(nums)):
            # If index out of range remove the index
            while (index_queue and index_queue[0] < i  - k + 1):
                index_queue.pop(0)
                
            # If within the k window (the behind data) is smaller that the current one, remove it
            while (index_queue and nums[index_queue[-1]] < nums[i]):
                index_queue.pop()
                
            index_queue.append(i)
            
            if (i >= k - 1):
                result.append(nums[index_queue[0]])
            
        return result