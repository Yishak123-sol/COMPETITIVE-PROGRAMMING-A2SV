class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        
        heap = []
        for i in range(len(heights)-1):
            
            diff = heights[i+1] - heights[i]
            
            if diff > 0:
                
                if ladders:
                    heapq.heappush(heap, diff)
                    ladders -= 1
                    
                elif heap and diff > heap[0]:
                    heapq.heappush(heap, diff)
                    bricks -= heapq.heappop(heap)
                    
                else:bricks -= diff
                if bricks < 0:return i
                    
        return len(heights)-1