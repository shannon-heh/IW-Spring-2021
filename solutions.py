# Depth-first search
def dfs(node, explored):
    if node not in explored:
        explored.append(node)
        for neighbor in node.neighbors:
            dfs(neighbor, explored)

    return explored

# Breadth-first search


def bfs(start, goal):
    explored = []
    queue = []
    start_path = []
    start_path.append(start)
    queue.append(start_path)

    while (len(queue) > 0):
        first_path = queue.pop(0)
        last_node = first_path[len(first_path)-1]
        if last_node not in explored:
            for neighbor in last_node.neighbors:
                new_path = list(first_path)
                new_path.append(neighbor)
                queue.append(new_path)
                if neighbor == goal:
                    return new_path
            explored.append(last_node)
