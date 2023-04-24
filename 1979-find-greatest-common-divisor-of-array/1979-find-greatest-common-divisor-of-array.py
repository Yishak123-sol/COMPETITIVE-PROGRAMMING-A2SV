class Solution:
    def findGCD(self, nums: List[int]) -> int:
        
        maxNum = minNum = nums[0]
        
        for i in range(1, len(nums)):
            if nums[i] > maxNum:
                maxNum = nums[i]
                
            elif nums[i] < minNum:
                minNum = nums[i]
        
        multi_of_two = minNum * maxNum
        temp = minNum
        while temp:
            if minNum % temp == 0 and maxNum % temp == 0:return temp
            temp -= 1
            
        
        