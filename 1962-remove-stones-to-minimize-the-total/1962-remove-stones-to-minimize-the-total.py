class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        
        for i in range(len(piles)):
            piles[i] = -piles[i]
            
        heapq.heapify(piles)
        
        while k:
        
            curr = heapq.heappop(piles) * -1
            pile_floor = math.ceil(curr/2)
            print(pile_floor)
            k -= 1
            
            heapq.heappush(piles, -pile_floor)
        
        return sum(piles) * -1
            