class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:

        temp = {}
        left = 0
        length = len(p)
        p = Counter(p)
        ans = []
        
        for right in range(len(s)):
            if s[right] in temp:
                temp[s[right]] += 1
            else:
                temp[s[right]] = 1
            
            if (right-left+1) == length:
                if temp == p:
                    ans.append(left)
                
                temp[s[left]] -= 1

                if temp[s[left]] == 0:
                    del temp[s[left]]

                left += 1

        return ans        
