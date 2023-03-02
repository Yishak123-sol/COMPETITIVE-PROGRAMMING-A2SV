class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        
        # time_taken = 0
        length = len(tickets)
#         for i in range(length*100+2):
            
#             if tickets[k%length] == 0:
#                 return time_taken

#             if tickets[i%length] != 0:
#                 tickets[i%length] -= 1 
#                 time_taken += 1

        sold_Tickets = 0
        deductions = 0
        
        for i in range(length):
            if tickets[i] >= tickets[k]:
                sold_Tickets += tickets[k]
            else:
                sold_Tickets += tickets[i]
                
            if i > k and tickets[i] >= tickets[k]:
                deductions += 1
                
        time_taken = sold_Tickets - deductions
        
        return time_taken
    
    
    
    