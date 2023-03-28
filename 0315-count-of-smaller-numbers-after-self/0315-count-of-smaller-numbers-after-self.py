from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        s = SortedList()
        out = []
        
        for num in nums[::-1]:
            ans = SortedList.bisect_left(s, num)
            out.append(ans)
            s.add(num)
            
        return reversed(out)