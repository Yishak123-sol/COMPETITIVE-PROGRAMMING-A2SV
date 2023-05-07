import heapq
class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        
        for i in range(len(tasks)):
            tasks[i].append(i)
        
        heapq.heapify(tasks)
        time = tasks[0][0]
        available = []
        ans = []
        while tasks or available:
            
            while tasks and time >= tasks[0][0]:
                
                task = heapq.heappop(tasks)
                available_task = (task[1], task[2])
                heapq.heappush(available, available_task)
                
            if available:
                processing_task = heapq.heappop(available)
                time += processing_task[0]
                ans.append(processing_task[1])
            else:
                time = tasks[0][0]
                
        return ans
                
                
                