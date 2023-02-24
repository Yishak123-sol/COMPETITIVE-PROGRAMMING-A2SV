class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        hahmap = defaultdict(lambda:-1)
        stack = []
        for num in nums2:
            while stack and stack[-1] < num:
                hahmap[stack[-1]] = num
                stack.pop()

            stack.append(num)
        
        return [hahmap[num] for num in nums1]