'''

Well this is the easiest way to get things done, but the complexity is nklog(k)
For nk solution, you can construct a hashmap where the key contains a 26-long-tuple that store the number
of characters shows up in each string
Ex: "bad" -> (1,1,0,1,0,0,0,...,0)

'''

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        my_dict = {}
        
        for word in strs:
            temp_list = tuple(sorted(word))
            
            if (temp_list in my_dict):
                my_data = my_dict[temp_list]
                my_data.append(word)
                my_dict[temp_list] = my_data
            else:
                my_dict[temp_list] = [word]
        
        return my_dict.values()