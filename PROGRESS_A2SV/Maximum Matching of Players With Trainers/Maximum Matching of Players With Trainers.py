class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:

        players.sort()
        trainers.sort()
        count = 0
        index = 0

        for i in range(len(players)):
            if index < len(trainers) and players[i] <= trainers[index]:
                count += 1
                index += 1
            else:
                while index < len(trainers) and players[i] > trainers[index]:
                    index += 1
                
                if index < len(trainers) and players[i] <= trainers[index]:
                    count += 1
                    index += 1

            
        return count
