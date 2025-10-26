class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}

        def backtrack(steps):
            # Base cases
            if steps == 0:
                return 1
            if steps < 0:
                return 0
            
            # Return cached result
            if steps in memo:
                return memo[steps]
            
            # Recursive relation: climb 1 or 2 steps
            memo[steps] = backtrack(steps - 1) + backtrack(steps - 2)
            return memo[steps]

        return backtrack(n)


    def climbStairs(self, n: int) -> int:
        fib_list = [1,1]
        
        for i in range(2, n + 1):
            fib_list.append(fib_list[i - 2] + fib_list[i - 1])
            
        return fib_list[n]

