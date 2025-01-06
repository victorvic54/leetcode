class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        answer = []
        for i in range(len(boxes)):
            total_operations = 0
            for j in range(len(boxes)):
                if i == j:
                    continue
                
                if boxes[j] == '1':
                    total_operations += abs(j - i)
            answer.append(total_operations)
        return answer


    #   1   0   0  1  0  1   1
    # [ 4,  3,  3, 3, 2, 2,  1]
    # [14, 12, 10, 8, 8, 8, 10]
    def minOperations(self, boxes: str) -> List[int]:
        prefix_count = 0
        total_val = 0
        for i in range(len(boxes)):
            if boxes[i] == '1':
                prefix_count += 1
                total_val += i

        answer = []
        suffix_count = 0
        for i in range(len(boxes)):
            answer.append(total_val)
            if boxes[i] == '1':
                prefix_count -= 1
                suffix_count += 1
            total_val = total_val - prefix_count + suffix_count
        return answer

