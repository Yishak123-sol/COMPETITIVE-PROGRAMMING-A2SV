class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        ans = []

        for i in range(len(arr), 1, -1):

            index = arr.index(i)
            ans.append(index+1)
            ans.append(i)
            arr = arr[:index:-1] + arr[:index]
            

        
        return ans
