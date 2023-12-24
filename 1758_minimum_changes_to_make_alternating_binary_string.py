class Solution:
    def minOperations(self, s: str) -> int:
        leading_zero = 0
        leading_one = 0
        for i in range(len(s)):
            if i % 2 == 0:
                if s[i] != '0':
                    leading_zero += 1
                else:
                    leading_one += 1
            else:
                if s[i] != '1':
                    leading_zero += 1
                else:
                    leading_one += 1

        # leading_one = len(s) - leading_zero
        return min(leading_zero, leading_one)

