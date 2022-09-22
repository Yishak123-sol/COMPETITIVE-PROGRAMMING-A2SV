class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        length = len(arr)
        check_point = length//2
        arr = Counter(arr)
        count_list = []
        if len(arr) <= 2:
            return 1
        
        for i, j in arr.most_common(length):
            count_list.append(j)
            
        
        sum = count_list[0]
        count = 1
        while sum < check_point:
            sum += int(count_list[count])
            count += 1
            
        return count
