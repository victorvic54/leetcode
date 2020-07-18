class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        # Create factorial for tracking
        tmp_list = [1]
        
        for i in range(1, n):
            tmp_list.append(tmp_list[i - 1] * i)
        
        result = ""
        num_list = [str(i+1) for i in range(n)]  # just a number ["1", "2", ... n]
        
        # Not modifying the initial value
        counter = n
        position = k - 1
        
        while (counter != 0):
            index_to_pick = int(position / tmp_list[counter - 1])
            result += num_list[index_to_pick]
            
            num_list.remove(num_list[index_to_pick])
            position = position % tmp_list[counter - 1]
        
            counter -= 1
        
        return str(result)


# Visualization:
# position  permute:
#    0       1234
#    1       1243
#    2       1324
#    3       1342
#    4       1423
#    5       1432
#    6       2134
#    7       2143
#    8       2314
#    9       2341
#    10      2413
#    11      2431
        