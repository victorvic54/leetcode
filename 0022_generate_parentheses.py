class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(opening, closing, num_open, tmp_result, results):
            if (len(tmp_result) == 2 * n):
                results.append(tmp_result)
            
            if (opening > 0):
                generate(opening - 1, closing, num_open + 1, tmp_result + "(", results)
            
            if (closing > 0):
                if (num_open > 0):
                    generate(opening, closing - 1, num_open - 1, tmp_result + ")", results)
            
        results = []
        generate(n, n, 0, "", results)
        
        return results