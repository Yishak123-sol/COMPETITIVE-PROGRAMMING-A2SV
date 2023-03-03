class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        minval = 1
        maxval = max(piles)
        curr_mid = math.inf
        
        while minval <= maxval:
            
            speed = minval + (maxval-minval)//2
            hours = 0
            
            for i in range(len(piles)):
                if piles[i]<= speed:
                    hours += 1
                else:
                    hours += math.ceil(piles[i]/speed)
                    
            if hours <= h:
                curr_mid = min(curr_mid, speed)
                maxval = speed - 1
            else:
                minval = speed + 1
    
        return curr_mid
                
                    
                