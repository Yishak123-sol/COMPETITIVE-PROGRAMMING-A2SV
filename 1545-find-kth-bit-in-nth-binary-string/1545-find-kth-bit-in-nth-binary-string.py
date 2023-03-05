class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        output = self.changeInbinary(n, k)
        return output[k-1]
    
    def changeInbinary(self, n, k):
        
        if n == 1: return "0"
        output = self.changeInbinary(n-1, k)
        
        temp = list(output)
        for i in range(len(output)):
            if temp[i] == "0":
                temp[i] = "1"
            else:
                temp[i] = "0"
                
        return output + "1" + "".join(temp[::-1])
    

        