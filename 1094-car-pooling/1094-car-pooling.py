class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        
        passenger_counts = [0]*1003
        
        for passengers, start, end in trips:
            passenger_counts[start] += passengers
            passenger_counts[end] -= passengers
            
        current_capacity = 0
        for i in range(1003):
            current_capacity += passenger_counts[i]
            if current_capacity > capacity:return False
        return True