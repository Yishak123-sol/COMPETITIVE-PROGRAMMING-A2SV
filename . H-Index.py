class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations = sorted(citations)
        index = 0
        output = 0 
        while index < len(citations):
            if citations[index] >= len(citations) - index:
                output = len(citations) - index
                
                return output
            
            index += 1
        
        return 0
        
