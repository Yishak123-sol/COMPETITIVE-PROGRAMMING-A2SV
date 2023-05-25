from collections import defaultdict
import sys
import threading

def main():
    def Bipartite(graph, colors, n):

        for node in range(1, n+1):
            if colors[node] == None:
                if dfs(node, colors, graph) == 'NOT BICOLOURABLE.':
                    return 'NOT BICOLOURABLE.'

        return 'BICOLOURABLE.'
                

    def dfs(node, colors, graph):

        if colors[node] == None:
            colors[node] = False

        for neighbor in graph[node]:
            if colors[neighbor] == None:
                colors[neighbor] = not colors[node]
                dfs(neighbor, colors, graph) 
            else:
                if colors[neighbor] == colors[node]:
                    return 'NOT BICOLOURABLE.'
                
        return 'BICOLOURABLE.'
                

    while True:
        n = int(input())
        if not n:
            break

        edges = int(input())
        graph = defaultdict(list)
        colors = [None]*(n+1)
        for _ in range(edges):
            node1, node2 = list(map(int, input().split()))
            graph[node1-1].append(node2-1)
            graph[node2-1].append(node1-1)

        print(Bipartite(graph, colors, n))
    

sys.setrecursionlimit(1 << 30)
threading.stack_size(1 << 27)
main_thread = threading.Thread(target = main)
main_thread.start()
main_thread.join()
