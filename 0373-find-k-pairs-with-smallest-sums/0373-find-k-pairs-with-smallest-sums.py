class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        heap = []
        
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                
                curr_sum = nums1[i] + nums2[j]
                heapq.heappush(heap, (-curr_sum, nums1[i], nums2[j]))
                
                if len(heap) > k:
                    pairSum, num1, num2 = heapq.heappop(heap)
                    if -pairSum <= curr_sum:
                        break
                        
        result = [pair[1:] for pair in heap]
        
        return result
                        