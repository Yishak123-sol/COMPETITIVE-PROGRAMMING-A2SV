class Solution:
    def addBinary(self, a: str, b: str) -> str:
        
        first_num = 0
        count = 0
        for i in range(len(a)-1, -1, -1):
            if a[i] == "1":
                first_num += (2**count)
            count += 1
        
        second_num = 0
        count = 0
        for i in range(len(b)-1, -1, -1):
            if b[i] == "1":
                second_num += (2**count)
            count += 1
        
        total = first_num + second_num
        res = bin(total)
        
        return res[2:]
        
       
        