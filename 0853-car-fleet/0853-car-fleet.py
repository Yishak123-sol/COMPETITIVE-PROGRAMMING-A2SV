class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        for i in range(len(position)):
            curr_position = target - position[i]
            position[i] = (curr_position, curr_position / speed[i])
        position.sort()
        
        count_carfleet = temp = 0
        for j in range(len(position)):
            if position[j][1] > temp:
                temp = position[j][1]
                count_carfleet += 1

        return count_carfleet
        