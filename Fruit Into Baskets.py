class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        
        if len(fruits)==1:
            return 1
        elif len(fruits)==2:
            return 2
        
        left, right = 0, 0
        max_sum = 0
        dic = {}
        while right< len(fruits):
            dic[fruits[right]] = right
            if len(dic) >= 3:
                min_value = min(dic.values())
                del dic[fruits[min_value]]
                left = min_value + 1
                
            max_sum = max(max_sum, right-left+1)
            right += 1
            
        return max_sum
