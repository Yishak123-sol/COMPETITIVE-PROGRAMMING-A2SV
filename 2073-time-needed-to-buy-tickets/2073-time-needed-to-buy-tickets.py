class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        time_taken = 0
        length = len(tickets)
        for i in range(length*100+2):
            
            if tickets[k%length] == 0:
                return time_taken

            if tickets[i%length] != 0:
                tickets[i%length] -= 1 
                time_taken += 1
            