class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if (not matrix):
            return False
        
        row = len(matrix)
        col = len(matrix[0])
        
        row_to_search = -1
        for i in range(1, row):
            if (target < matrix[i][0]):
                row_to_search = i - 1
                break
        
        left = 0
        right = col - 1
        
        # implement binary search here
        while (left <= right):
            mid = (left + right) // 2
            value_to_search = matrix[row_to_search][mid]
            
            if (value_to_search == target):
                return True
            elif (value_to_search < target):
                left = mid + 1
            else:
                right = mid - 1
            
        return False
