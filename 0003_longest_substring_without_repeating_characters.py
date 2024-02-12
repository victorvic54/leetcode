
# First solution
# Use this example:
#
#   1 2 3 4 4 3 4 -> longest
#   0 1 2 3 4 5 6 -> index
#   a b c e a c b
#
# Keep track of the longest (max) value for every index. Store it in a dictionary
#
# Another edge case:
# 
# 012345
# abddba
# 123123

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
        counter = 0
        my_dict = dict()
        arr = [0] * len(s)
        
        if (s == ""):
            return 0
        
        for i in range(len(s)):
            char = s[i]
            
            if (char in my_dict):
                counter = min(i - my_dict[char], arr[i-1] + 1)
            else:
                counter += 1
            
            my_dict[char] = i
            arr[i] = counter
        
        
        return max(arr)


# Third solution

class Solution:
    """
    012345678
    abccbcdba
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        length = 0
        char_dict = {}
        for i in range(len(s)):
            if s[i] not in char_dict:
                length += 1
                char_dict[s[i]] = i
            else:
                if i - char_dict[s[i]] > length:
                    length += 1
                else:
                    length = i - char_dict[s[i]]
                char_dict[s[i]] = i
            
            ans = max(ans, length)

        return ans
            
            
            


