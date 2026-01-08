class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        memo = {}
        def backtracking(has_selected, i, j):
            if (has_selected, i, j) in memo:
                return memo[(has_selected, i, j)]

            if i >= len(nums1) or j >= len(nums2):
                if has_selected:
                    return 0
                return -float('inf')
            
            max_product = -float('inf')
            max_product = max(max_product, backtracking(has_selected, i + 1, j))
            max_product = max(max_product, backtracking(has_selected, i, j + 1))
            max_product = max(max_product, (nums1[i] * nums2[j]) + backtracking(True, i + 1, j + 1))
            memo[(has_selected, i, j)] = max_product
            return max_product
        
        return backtracking(False, 0, 0)
