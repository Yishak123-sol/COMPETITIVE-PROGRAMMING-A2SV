class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        
        for j in range(len(words)):
            for i in range(ord('a'), ord('z')+1):
                curr = chr(i)
                count = 0
                for char in words[j]:
                    if curr == char:
                        count += 1
                if count > 0:
                    break
            words[j] = count
        words.sort()
            
        for i in range(len(queries)):
            for j in range(ord('a'), ord('z')+1):
                curr = chr(j)
                count = 0
                for char in queries[i]:
                    if char == curr:
                        count += 1
                if count > 0:
                    break
            queries[i] = count 
    
        length = len(words)
        result = []
        for querie in queries:
            left, right = 0, length-1
            while left <= right:
                mid = left + (right - left)//2
                if querie >= words[mid]:
                    left = mid + 1
                else:
                    right = mid - 1
                    
            result.append(length - left)
            
        return result
        
            
                