class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_time = []
        for i in range(len(position)):
            position_time.append([position[i],    (target-position[i]) / speed[i] ])


        position_time = sorted(position_time, reverse=True)
        count = 0
        temp = 0
        for i in range(len(position_time)):
            if position_time[i][1] > temp :
                temp = position_time[i][1]
                count += 1

        return count
