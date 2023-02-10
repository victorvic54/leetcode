class Solution:
    def countBits(self, num: int) -> List[int]:
        result = [0]
        
        index = 0
        target = 1
        
        for i in range(0, num):
            if (target - 1 == i):
                index = 0
                target *= 2
                result.append(result[index] + 1)
            else:
                index += 1
                result.append(result[index] + 1)
                
        return result