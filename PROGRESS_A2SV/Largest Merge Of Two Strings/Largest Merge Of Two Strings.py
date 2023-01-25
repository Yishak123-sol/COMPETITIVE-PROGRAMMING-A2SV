class Solution:
    def largestMerge(self, word1: str, word2: str) -> str:

        length1 = len(word1)
        length2 = len(word2)
        i, j = 0, 0
        ans = []

        while i < length1 and j < length2:

            if word1[i:] >= word2[j:]:
                ans.append(word1[i])
                i += 1

            else:
                ans.append(word2[j])
                j += 1
        
        while j < length2:
            ans.append(word2[j])
            j += 1
        
        while i < length1:
            ans.append(word1[i])
            i += 1
            

        merge = "".join(ans)
        return merge
