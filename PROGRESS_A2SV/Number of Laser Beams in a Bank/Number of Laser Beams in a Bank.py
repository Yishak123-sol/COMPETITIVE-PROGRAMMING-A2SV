class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:

        arr = []
        total = 0

        for i in range(len(bank)):
            count_one = 0
            for j in range(len(bank[0])):
                if int(bank[i][j]) == 1:
                    count_one += 1
            
            if arr:
                total += arr[-1] * count_one
                
            if count_one >= 1:
                arr.append(count_one)
            

        return total
