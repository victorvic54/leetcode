class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        '''
        1. For any array whose length is l, the first missing positive must be in range [1,...,l+1], 
            so we only have to care about those elements in this range and remove the rest.
        2. We can use the array index as the hash to restore the frequency of each number within 
            the range [1,...,l+1], we add the number by len(nums)
        3. Since we add all number with len(nums) except one index value that is not in our list,
            any number that is lower than len(nums) shall be the answer
        '''
        
        # To handle duplicate value such as: [2, 2]
        # We append 0 because we want to count from index 1 instead of index 0
        nums = list(set(nums)) + [0]
        n = len(nums)
        
        for i in range(len(nums)):  # delete those useless elements
            if nums[i]<0 or nums[i]>=n:
                nums[i]=0
        
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            nums[nums[i] % n] += n
        
        for i in range(1, len(nums)):
            if nums[i] // n == 0:
                return i
        
        return n