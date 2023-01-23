class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        
        piles.sort()

        nextMax_index = len(piles)-2
        index = 0
        total = 0
        
        while index < nextMax_index:

            total += piles[nextMax_index]
            nextMax_index -= 2
            index += 1
            
        return total
