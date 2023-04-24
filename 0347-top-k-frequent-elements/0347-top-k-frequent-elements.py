class Solution:
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        dic = {}

        for num in nums:

            if num not in dic:
                dic[num] = 1
            else:
                dic[num] += 1
        
        dic = sorted(dic.items(), key=lambda x: -x[1])
        print(dic)

        r = []

        for i in range(k):
            r.append(dic[i][0])
        
        return [dic[i][0] for i in range(k)]
        
            
        
            
                
                