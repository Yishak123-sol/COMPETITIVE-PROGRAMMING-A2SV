class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        montonicity = []
        prev = temp = inf
        for i in range(len(nums)):
            while montonicity and montonicity[-1] < nums[i]:
                if prev < montonicity[-1]:
                    return True
                temp = min(temp, montonicity.pop())
                
            prev = temp   
            montonicity.append(nums[i])
        
        return False