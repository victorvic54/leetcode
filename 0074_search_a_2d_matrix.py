class Solution:
    def bisect_right(self, arr, target):
        left = 0
        right = len(arr)
        while left < right:
            mid = (left + right) // 2
            if arr[mid] <= target:
                left = mid + 1
            else:
                right = mid
        return left


    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        x_list = [mat[0] for mat in matrix]
        x_idx = self.bisect_right(x_list, target) - 1
        if x_idx < 0:
            return False  # target is smaller than the first element in the matrix

        y_idx = self.bisect_right(matrix[x_idx], target) - 1
        return matrix[x_idx][y_idx] == target

# Time: O(log m + log n)
# Space: O(1)
