class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        sorted_score = sorted(score,key = lambda x: -x[k])
        return sorted_score
