class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        max_satisfaction = 0
        starting_index = 0
        while True:
            if starting_index == len(satisfaction):
                break

            counter = 0
            tmp_satisfaction = 0
            for i in range(starting_index, len(satisfaction)):
                counter += 1
                tmp_satisfaction += satisfaction[i] * counter
            
            max_satisfaction = max(max_satisfaction, tmp_satisfaction)
            starting_index += 1
        
        return max_satisfaction

