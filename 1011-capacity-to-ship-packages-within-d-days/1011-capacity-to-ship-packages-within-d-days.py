class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        low = max(weights)
        high = sum(weights)
        
    
        while low <= high:
            
            day = 1
            capacity = low + (high-low)//2
            total = 0
            
            for weight in weights:
                 
                if weight + total > capacity:
                    total = 0
                    day += 1
                    
                total += weight
                
            if day <= days:
                high = capacity - 1
            else:
                low = capacity + 1
            
                
        return low