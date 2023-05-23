class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.top_k_nums = sorted(nums)[-k:]
        self.k = k

    def add(self, val: int) -> int:
        if len(self.top_k_nums) >= self.k:
            if val <= self.top_k_nums[0]:
                return self.top_k_nums[0]
        
            self.top_k_nums = self.top_k_nums[1:]

        self.binary_insert(val)
        return self.top_k_nums[0]

    # or use heapq
    def binary_insert(self, val):
        left = 0
        right = len(self.top_k_nums)

        while left < right:
            mid = (left + right) // 2

            if self.top_k_nums[mid] < val:
                left = mid + 1
            else:
                right = mid
        
        self.top_k_nums.insert(left, val)


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
