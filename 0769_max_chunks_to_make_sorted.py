class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_number = 0
        chunk = 0
        for i in range(len(arr)):
            max_number = max(max_number, arr[i])
            if max_number == i:
                chunk += 1
            
        return chunk

