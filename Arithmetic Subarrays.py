class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        sub_arr = []
        answer = []
        for i in range(len(l)):
            bool_value = True
            sub_arr = nums[l[i]:r[i]+1]
            sub_arr.sort()

            for j in range(1, len(sub_arr)):
                if sub_arr[j] - sub_arr[j-1] != sub_arr[1] - sub_arr[0]:
                    bool_value = False

            answer.append(bool_value)
        return answer
