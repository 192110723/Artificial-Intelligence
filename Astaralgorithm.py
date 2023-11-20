import heapq

class Node:
    def __init__(self, state, parent=None, cost=0, heuristic=0):
        self.state = state
        self.parent = parent
        self.cost = cost
        self.heuristic = heuristic

    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

def astar(start, goal, heuristic_func, neighbors_func):
    open_set = []
    closed_set = set()

    start_node = Node(start, None, 0, heuristic_func(start, goal))
    heapq.heappush(open_set, start_node)

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.state == goal:
            path = []
            while current_node:
                path.insert(0, current_node.state)
                current_node = current_node.parent
            return path

        closed_set.add(current_node.state)

        for neighbor in neighbors_func(current_node.state):
            if neighbor not in closed_set:
                cost = current_node.cost + 1
                heuristic = heuristic_func(neighbor, goal)
                neighbor_node = Node(neighbor, current_node, cost, heuristic)
                heapq.heappush(open_set, neighbor_node)

    return None

# Example: A* algorithm for finding the path in a 2D grid
def grid_heuristic(state, goal):
    return abs(state[0] - goal[0]) + abs(state[1] - goal[1])

def grid_neighbors(state):
    x, y = state
    neighbors = [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]
    return [(nx, ny) for nx, ny in neighbors if 0 <= nx < 5 and 0 <= ny < 5]

start_point = (0, 0)
goal_point = (4, 4)

result = astar(start_point, goal_point, grid_heuristic, grid_neighbors)

if result:
    print("Path found:")
    for point in result:
        print(point)
else:
    print("No path found.")
