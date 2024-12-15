class ClassRatio:
    def __init__(self, passed, total_students):
        self.passed = passed
        self.total_students = total_students

    def __lt__(self, other):
        return ((self.passed + 1) / (self.total_students + 1)) - (self.passed / self.total_students) > \
            ((other.passed + 1) / (other.total_students + 1)) - (other.passed / other.total_students)

    def get_class_ratio(self):
        return self.passed / self.total_students


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        class_ratios = []
        for passed, total in classes:
            heapq.heappush(class_ratios, ClassRatio(passed, total))
        
        for i in range(extraStudents):
            class_ratio = heapq.heappop(class_ratios)
            heapq.heappush(class_ratios, ClassRatio(class_ratio.passed + 1, class_ratio.total_students + 1))
        
        avg_pass_ratio = 0
        for class_ratio in class_ratios:
            avg_pass_ratio += class_ratio.get_class_ratio()
        
        return avg_pass_ratio / len(class_ratios)
 
