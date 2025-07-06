class FindSumPairs:

    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums2 = nums2
        self.keys = sorted(self.freq1.keys())
        self.freq1 = Counter(nums1)
        self.freq2 = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.freq2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.freq2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for num1 in self.keys:
            if num1 >= tot:
                break
            if self.freq2[tot-num1]:
                ans += self.freq1[num1] * self.freq2[tot-num1]
        return ans

# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)

