"""
Solution TLE due to (n!) when doing the combination (7!)
Non TLE solution is insane
"""
class Solution:
    def findCombination(self, num):
        num_ls = list(num)
        all_combinations = set()

        def backtracking(path, remaining):
            if not remaining:
                if path[0] != '0':
                    all_combinations.add("".join(path))
                return

            for i in range(len(remaining)):
                backtracking(path + [remaining[i]], remaining[:i] + remaining[i+1:])

        backtracking([], num_ls)
        return all_combinations


    def countGoodIntegers(self, n: int, k: int) -> int:
        if n == 1:
            return len([i for i in range(1, 10) if i % k == 0])

        digits = [[]] * (n // 2)
        for i in range(n // 2):
            digits[i] = [j for j in range(10)]
            if i == 0:
                digits[i].remove(0)

        result = set()
        tmp_digits = [0] * n
        for prod in list(product(*digits)):
            for i in range(n // 2):
                tmp_digits[i] = str(prod[i])
                tmp_digits[n-1-i] = str(prod[i])
            
            if n % 2 != 0:
                for j in range(10):
                    tmp_digits[(n // 2)] = str(j)
                    new_digit = "".join(tmp_digits)
                    if new_digit in result:
                        continue
                    if int(new_digit) % k == 0:
                        combination = self.findCombination(new_digit)
                        result = result.union(combination)
            else:
                new_digit = "".join(tmp_digits)
                if new_digit in result:
                    continue
                if int(new_digit) % k == 0:
                    combination = self.findCombination(new_digit)
                    result = result.union(combination)

        return len(set(result))
