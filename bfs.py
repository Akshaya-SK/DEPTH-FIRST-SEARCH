from collections import deque

def bfs(graph, start):
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            for neighbor in graph[vertex]:
                if neighbor not in visited and neighbor not in queue:
                    queue.append(neighbor)
    return visited

def main():
    n, e = map(int, input("Enter number of nodes and edges: ").split())
    graph = {}

    print("Enter the edges (one per line):")
    for _ in range(e):
        u, v = input().split()
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph

    for node in graph:
        graph[node].sort()

    start_node = input("Enter the start node: ")
    traversal = bfs(graph, start_node)

    print("BFS Traversal Output:")
    print(traversal)

main()
