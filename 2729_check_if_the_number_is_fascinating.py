class Solution:
    def isFascinating(self, n: int) -> bool:
        final_list = list(str(n) + str(2 * n) + str(3 * n))
        if len(final_list) != 9:
            return False
        
        for i in range(1, 10):
            if str(i) not in final_list:
                return False

        return True

