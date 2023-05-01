class Solution:
    def average(self, salary: List[int]) -> float:
        total = 0
        min_val = float('inf')
        max_val = 0

        for val in salary:
            total += val

            if val > max_val:
                max_val = val
            
            if val < min_val:
                min_val = val
        
        return (total - min_val - max_val) / (len(salary) - 2)
