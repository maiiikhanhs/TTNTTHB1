import heapq

def a_star_algorithm(start, goal, graph, heuristic):
 
    # hang doi uu tien
    open_set = []
    heapq.heappush(open_set, (0 + heuristic[start], start))

    # duong di va chi phi
    came_from = {}
    g_score = {node: float('inf') for node in graph}
    g_score[start] = 0

    while open_set:
        current_f, current = heapq.heappop(open_set)

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path, g_score[goal]

        for neighbor, cost in graph[current]:
            tentative_g_score = g_score[current] + cost

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic[neighbor]
                heapq.heappush(open_set, (f_score, neighbor))

    return [], float('inf') 

# do thi va mau minh hoa
example_graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('D', 1)],
    'C': [('D', 1), ('E', 5)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': []
}

example_heuristic = {
    'A': 6,
    'B': 4,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

# chay thu
configs = [
    ('A', 'F', example_graph, example_heuristic),
    ('A', 'D', example_graph, example_heuristic),
    ('A', 'E', example_graph, example_heuristic),
    ('B', 'F', example_graph, example_heuristic),
    ('C', 'F', example_graph, example_heuristic)
]

for start, goal, graph, heuristic in configs:
    path, cost = a_star_algorithm(start, goal, graph, heuristic)
    print(f"Start: {start}, Goal: {goal}\nPath: {path}\nCost: {cost}\n")
