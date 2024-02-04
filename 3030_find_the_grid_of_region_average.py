class Solution:
    def isValidRegion(self, image, i, j, threshold):
        directions = [(0,1), (0,-1), (-1,0), (1,0)]
        limit_x = i + 2
        limit_y = j + 2
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                for direction in directions:     
                    next_x = x + direction[0]
                    next_y = y + direction[1]
                    if 0 <= next_x < len(image) and i <= next_x <= limit_x and 0 <= next_y < len(image[0]) and j <= next_y <= limit_y:
                        if abs(image[next_x][next_y]-image[x][y]) > threshold:
                            return False
        return True
        
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        counter_dp = [[0] * len(image[0]) for i in range(len(image))]
        val_dp = [[0] * len(image[0]) for i in range(len(image))]
        for i in range(0, len(image) - 2):
            for j in range(0, len(image[0]) - 2):
                total_sum = 0
                isValidRegion = self.isValidRegion(image, i, j, threshold)
                
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        total_sum += image[x][y]

                average_sum = total_sum // 9
                for x in range(i, i + 3):
                    for y in range(j, j + 3):
                        if isValidRegion:    
                            if counter_dp[x][y] == -1:
                                counter_dp[x][y] = 0
                                val_dp[x][y] = 0
                            counter_dp[x][y] += 1
                            val_dp[x][y] += average_sum
                        else:
                            if counter_dp[x][y] == 0:
                                counter_dp[x][y] = -1
                                val_dp[x][y] = image[x][y]

        for x in range(0, len(image)):
            for y in range(0, len(image[0])):
                if counter_dp[x][y] == -1:
                    continue
                val_dp[x][y] = val_dp[x][y] // counter_dp[x][y]
        
        return val_dp

