from collections import defaultdict, deque
def bfs(colors, graph):

    queue = deque()
    queue.append(1)
    while queue:
        node = queue.popleft()
        if colors[node] == None:
            colors[node] = False
        
        for neighbor in graph[node]:
            if colors[neighbor] == colors[node]:
                return 'NOT BICOLOURABLE.'
            
            if colors[neighbor] == None:
                queue.append(neighbor)

            colors[neighbor] = not colors[node]
    
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

    print(bfs(colors, graph))
