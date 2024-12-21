def dfs(graph, start, goal):

    stack = [(start, [start])] 
    visited = set()

    while stack:
        current, path = stack.pop()

        if current in visited:
            continue

        visited.add(current)

        if current == goal:
            return path  

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                stack.append((neighbor, path + [neighbor]))

    return []  # No path found
# Đồ thị ví dụ
example_graph = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D', 'E'],
    'D': ['F'],
    'E': ['F'],
    'F': []
}

# Các cấu hình đầu vào
configs = [
    ('A', 'F', example_graph),
    ('A', 'D', example_graph),
    ('A', 'E', example_graph),
    ('B', 'F', example_graph),
    ('C', 'F', example_graph)
]

# Chạy thử thuật toán DFS trên từng cấu hình
for start, goal, graph in configs:
    path = dfs(graph, start, goal)
    print(f"Start: {start}, Goal: {goal}\nPath: {path}\n")

