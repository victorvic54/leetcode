class Solution:
    def countAndSay(self, n: int) -> str:
        result = "1"
        
        for i in range(n - 1):
            curr_str = ""
            tmp_char = ""
            counter = 0
            
            for j in range(len(result)):
                if (j == 0):
                    tmp_char = result[0]
                    counter = 1
                else:
                    if (result[j] == tmp_char):
                        counter += 1
                    else:
                        curr_str = curr_str + str(counter) + tmp_char
                        
                        tmp_char = result[j]
                        counter = 1
            
            curr_str = curr_str + str(counter) + tmp_char
            result = curr_str
        
        return result