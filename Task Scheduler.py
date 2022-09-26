class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        dic = {}
        for task in tasks:
            if task in dic:
                dic[task] += 1
            else:
                dic[task] = 1
        
        values = [value for key, value in dic.items()]
        max_task = max(values)
        max_tasks = values.count(max_task)
        
        return max(len(tasks), (max_task-1)*(n+1) + max_tasks)
