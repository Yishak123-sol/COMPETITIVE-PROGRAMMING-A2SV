class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:

        for i in range(len(nums)):

            num = str(nums[i])[::-1]
            nums.append(int(num))
    
        
        distinct_integers = set(nums)
        distinct_integers_count = len(distinct_integers)
    

        return distinct_integers_count
        
       
            
