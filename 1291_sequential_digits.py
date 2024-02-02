class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low_n, high_n = len(str(low)), len(str(high))
        digits = "123456789"
        ans = []
        for i in range(low_n, high_n + 1):
            for j in range(0, 10 - i):
                num = int(digits[j:j+i])
                if low <= num <= high:
                    ans.append(num)
        return ans
