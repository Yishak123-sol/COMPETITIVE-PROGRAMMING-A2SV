class MedianFinder:

    def __init__(self):
        
        self.minheap = []
        self.maxheap = []
        
    def addNum(self, num: int) -> None:
        
        heapq.heappush(self.maxheap, -num)
        while len(self.minheap) < len(self.maxheap):
            maxval = heapq.heappop(self.maxheap)
            heapq.heappush(self.minheap, -maxval)
            
        while self.maxheap and self.minheap[0] < -self.maxheap[0]:
            heapq.heappush(self.minheap, -heapq.heappop(self.maxheap))
            heapq.heappush(self.maxheap, -heapq.heappop(self.minheap))
            
    def findMedian(self) -> float:
        length = len(self.minheap) + len(self.maxheap)                        
        if length % 2 == 0:
            return (self.minheap[0] +  (-self.maxheap[0]))/2
        else:
            return self.minheap[0]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()