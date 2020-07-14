'''

This question is quite confusing, the idea here is that you want to be greedy as much as you can
since you can choose to jump any number between [1, nums[index]] and 
its nums[index] doesn't neccessarily lands on the last index of the array

So it is like solving problem:
Given a list of number, which combination of number will raise the largest number quickly from left to right

If you still dont get it, think it if you walk through from the back of the list to the front
You want to find the left most index that can reach the position that you are currently in from the back.
But this solution is O(n^2)

Now think it forward: it will be O(n)

'''

class Solution:
    def jump(self, nums: List[int]) -> int:
        curr_end = 0
        curr_max = 0
        result  = 0
        
        for i in range(len(nums) - 1):
            curr_max = max(curr_max, i + nums[i])
            
            if (i == curr_end):
                result += 1
                curr_end = curr_max
            
        return result