class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        
        sums = []
        for i in range(len(nums1)):
            
            curSum = nums1[i]
            for j in range(len(nums2)):
                curSum += nums2[j]
                heapq.heappush(sums, (-curSum, nums1[i], nums2[j]))

                if len(sums) > k:
                    (summ,a,b) = heapq.heappop(sums)
                    
                    if summ >= -curSum:
                        break

                curSum = nums1[i]
        print(sums)
        return [i[1:] for i in sums]