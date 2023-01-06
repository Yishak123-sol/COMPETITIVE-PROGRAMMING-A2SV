
class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:

        costs.sort()
        costs_of_ice = 0
        count_ice = 0

        for i in range(len(costs)):

            costs_of_ice += costs[i]

            if costs_of_ice > coins:
                return count_ice

            count_ice = i+1
        
        return count_ice
