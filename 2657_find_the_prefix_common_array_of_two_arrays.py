class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        visited = set()
        common_count = 0
        common_arr = []

        for a, b in zip(A, B):
            if a in visited:
                common_count += 1
            else:
                visited.add(a)
            
            if b in visited:
                common_count += 1
            else:
                visited.add(b)

            common_arr.append(common_count)
        return common_arr


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        s = set()
        C = []
        for i in range(len(A)):
            s.add(A[i])
            s.add(B[i])
            C.append(2 * (i + 1) - len(s))
        return C

