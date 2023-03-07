class Solution:
    def calculate_trip_cost(self, timeList, target_time):
        result = 0
        for time in timeList:
            result += (target_time // time)
        return result

    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        left, right = 1, totalTrips * min(time)

        while left < right:
            mid = (left + right) // 2
            
            trip_cost = self.calculate_trip_cost(time, mid)
            if trip_cost >= totalTrips:
                right = mid
            else:
                left = mid + 1

        return left

