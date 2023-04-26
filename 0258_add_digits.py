class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            tmp_sum = 0
            while num:
                tmp_sum += num % 10
                num = num // 10
                
            num = tmp_sum

        return num
