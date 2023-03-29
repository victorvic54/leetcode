class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort()

        starting_index = 0
        max_satisfaction = 0
        while starting_index < len(satisfaction):
            counter = 0
            tmp_satisfaction = 0
            for i in range(starting_index, len(satisfaction)):
                counter += 1
                tmp_satisfaction += satisfaction[i] * counter
            
            max_satisfaction = max(max_satisfaction, tmp_satisfaction)
            starting_index += 1
        
        return max_satisfaction

