class Solution:
    
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        str_to_int = list(map(int, nums))
        sort_the_list = sorted(str_to_int)
        answer = str(sort_the_list[-k])
        
        return answer
