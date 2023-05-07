class Solution:
    def isPossible(self, nums):
        
        frequency = defaultdict(int)
        for num in nums:
            frequency[num] += 1
            
        subsequences = defaultdict(int)
        for num in nums:
            
            if frequency[num] == 0:
                continue
                
            frequency[num] -= 1
            if subsequences[num - 1] > 0:
                subsequences[num - 1] -= 1
                subsequences[num] += 1


            elif frequency[num + 1] > 0 and frequency[num + 2] > 0:
                subsequences[num + 2] += 1
                frequency[num + 1] -= 1
                frequency[num + 2] -= 1
                
            else:
                return False

        return True