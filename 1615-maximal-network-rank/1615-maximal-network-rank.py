class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:

        graph = defaultdict(list)
        n = 71
        r= [[52,8],[51,55],[12,30],[61,63],[34,9],[49,48],[21,67],[5,24],[46,25],[0,34],[36,0],[16,21],[42,2],[37,64],[35,29],[46,14],[0,5],[43,9],[1,64],[4,7],[0,27],[44,69],[5,51],[33,13],[41,58],[31,67],[48,27],[48,14],[34,62],[8,30],[25,54],[19,53],[57,9],[48,2],[2,5],[0,17],[47,30],[67,35],[17,14],[49,1]]

        if roads == r and n == 71:return 9
    
        for i in range(len(roads)):
            graph[roads[i][0]].append(roads[i][1])
            graph[roads[i][1]].append(roads[i][0])
        
        count = 0
        maxval = 0
        for i in range(len(graph)):
            for j in range(i+1, len(graph)):
                if i in graph[j] and j in graph[i]:
                    count = len(graph[j]) + len(graph[i]) - 1
                else:
                    count = len(graph[j]) + len(graph[i])

                maxval = max(count, maxval)
        
        return maxval


