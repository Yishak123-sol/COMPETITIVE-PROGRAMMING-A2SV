class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer  = []
        mult = 1
        zerocount = 0
        
        for i in nums:
            if i == 0:
                zerocount += 1
            else:
                mult *= int(i)
            
        for j in nums:
            if j == 0:
                if zerocount == 1:
                    answer.append(mult)
                else:
                    answer.append(0)
            else:   
                if zerocount == 0:
                    answer.append(mult//j)
                else:
                    answer.append(0)
            
        return answer
