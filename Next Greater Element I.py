class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums3 = []
        for i in nums1:
            add = False
            index = nums2.index(i)
            for j in range(index, len(nums2)):
                if nums2[j] > i:
                    nums3.append(nums2[j])
                    add = True
                    break
                    
            if not add:
                nums3.append(-1)
            
        return nums3
