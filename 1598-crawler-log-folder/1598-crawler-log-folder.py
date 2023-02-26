class Solution:
    def minOperations(self, logs: List[str]) -> int:
        
        CrawlerLog = []
        
        for i in range(len(logs)):
            
            if logs[i] == "../" and CrawlerLog:
                CrawlerLog.pop()
                
            elif logs[i] != "./" and logs[i] != "../":
                CrawlerLog.append(logs[i])
        
        return len(CrawlerLog )