
# First solution
# Use this example:
#
#   1 2 3 4 4 3 4 -> longest
#   0 1 2 3 4 5 6 -> index
#   a b c e a c b
#
# Keep track of the longest (max) value for every index. Store it in a dictionary


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        my_dict = dict()
        
        result, temp = 0, 0
        
        for i in range(len(s)):
            char = s[i]
            
            if (char in my_dict):
                temp = max(temp, my_dict[char] + 1)

            my_dict[char] = i
            result = max(result, i - temp + 1)
            
        return result


# Second solution:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        longest = 0
        my_set = set()
        
        for i in range(len(s)):
            char = s[i]
            
            if (char in my_set):
                if (len(my_set) > longest):
                    longest = len(my_set)
                
                for j in range(start, i):
                    my_set.remove(s[j])
                    start += 1
                    
                    if (s[j] == char):
                        break    
            
            my_set.add(char)
            
        return max(len(my_set), longest)
            