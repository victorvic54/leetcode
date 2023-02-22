class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:
        def is_feasible_within_days(max_weight):
            needed_days = 1
            tmp_weight = 0
            
            for weight in weights:
                tmp_weight += weight

                if tmp_weight > max_weight:
                    needed_days += 1
                    tmp_weight = weight

                if needed_days > D:
                    return False

            return True

        low, hi = max(weights), sum(weights)
        while low < hi:
            mid = (low + hi) // 2
            if is_feasible_within_days(mid):
                hi = mid
            else:
                low = mid + 1
                
        return low

