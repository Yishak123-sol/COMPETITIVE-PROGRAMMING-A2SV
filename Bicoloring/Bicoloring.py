from collections import defaultdict
import sys
import threading

def main():
    def Bipartite(graph, colors, n):

        visited = set()
        result = [False]
        for node in range(1, len(graph)):
            if result[0]:
                return 'NOT BICOLOURABLE.'
            if node not in visited:
                dfs(node, colors, visited, graph, result)

        return 'NOT BICOLOURABLE.' if result[0] else 'BICOLOURABLE.'

    def dfs(node, colors, visited, graph, result):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                colors[neighbor] = not colors[node]
                dfs(neighbor, colors, visited, graph, result)
                if result[0]:
                    return
            else:
                if colors[neighbor] == colors[node]:
                    result[0] = True
                    return

    while True:
        n = int(input())
        if not n:
            break

        edges = int(input())
        graph = defaultdict(list)
        colors = [False]*n
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
