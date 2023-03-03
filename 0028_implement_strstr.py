'''
This is an elegant solution of O(n). There is a lot of variation on using
this technique (KMP). Quite long for an easy problem but you can do this in python:

haystack.find(needle)

and you get the damn answer  :)
'''

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        
        if (needle == ""):
            return 0
        
        # Initialize KMP array
        # Check whether you know KMP:
        # given a pattern: "aabaabaaa"
        # return KMP_arr of [0, 1, 0, 1, 2, 3, 4, 5, 2]
        
        needle_arr = [None] * len(needle)
        needle_arr[0] = 0
        
        i = 0
        
        # There is a pointer i and j in the pattern
        for j in range(1, len(needle)): 
            if (needle[i] == needle[j]):
                needle_arr[j] = i + 1
                i += 1
            else:
                # If it is different, I want to:
                checked = False
                i = needle_arr[j - 1]       # 1. Go back to previous of curr_index and retrieve the value
                
                # I want to go back until I reached the initial index arr if
                # there is no character that is matched. It means there is no substring 
                # that is in the previous index of j
                while (i > 0):
                    if (needle[i] == needle[j]):                    
                        needle_arr[j] = i + 1
                        checked = True
                        break
                    
                    i = needle_arr[i - 1]
                
                # If it has reached the first index of the pattern, check if the character is the same with jth index
                if (not checked):
                    if (needle[i] == needle[j]):
                        needle_arr[j] = 1
                        i += 1
                    else:
                        needle_arr[j] = 0
        
        pointer = 0
        
        # Comparison of the string (haystack) with the pattern
        for i in range(len(haystack)):
            if (haystack[i] == needle[pointer]):
                if (len(needle) == pointer + 1):
                    return i - len(needle) + 1

                pointer += 1
            else:
                while (pointer > 0):
                    # need to go back to previous pattern
                    pointer = needle_arr[pointer - 1]
                
                    if (haystack[i] == needle[pointer]):
                        pointer += 1
                        break
        
        return -1
                
