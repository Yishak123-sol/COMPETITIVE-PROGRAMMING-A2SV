class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        orderd_list = []
        if len(changed)%2 != 0:
            return []

        changed.sort()
        count = Counter(changed)
        print(count)
        for i in changed:
            if i in count and count[i] >= 1:
                count[i] -=1
                if (i*2) in count and count[i*2] >= 1:
                    orderd_list.append(i)
                    count[i*2] -= 1
                    
        return orderd_list if len(orderd_list) == len(changed)//2 else []
