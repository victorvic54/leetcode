class Solution:
    def get_divisors(self, num):
        divisors = set()
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.add(i)
                divisors.add(num // i)
        return divisors

    def sumFourDivisors(self, nums: List[int]) -> int:
        total = 0
        for num in nums:
            divisors = self.get_divisors(num)
            if len(divisors) != 4:
                continue
            
            total += sum(divisors)
        return total

