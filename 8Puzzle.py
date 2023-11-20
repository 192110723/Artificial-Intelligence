import heapq
class PuzzleNode:
    def init(self, state, parent=None, action=None, cost=0):
        self.state = state
        self.parent = parent
        self.action = action
        self.cost = cost
        self.heuristic = self.calculate_heuristic()
    def calculate_heuristic(self):       
        misplaced = sum([1 if self.state[i] != i+1 else 0 for i in range(8)])
        return misplaced
    def lt(self, other):        
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)
def get_blank_index(state):
    return state.index(0)
def get_neighbors(state):
    blank_index = get_blank_index(state)
    neighbors = []   
    moves = [(0, -1), (0, 1), (-1, 0), (1, 0)]
    for move in moves:
        new_index = blank_index + move[0] + 3 * move[1]        
        if 0 <= new_index < 9:
            new_state = list(state)
            new_state[blank_index], new_state[new_index] = new_state[new_index], new_state[blank_index]
            neighbors.append(new_state)
    return neighbors
def a_star_search(initial_state):
    initial_node = PuzzleNode(initial_state)
    open_set = [initial_node]
    closed_set = set()
    while open_set:
        current_node = heapq.heappop(open_set)
        closed_set.add(tuple(current_node.state))
        if current_node.state == [1, 2, 3, 4, 5, 6, 8, 7, 0]:
            # Puzzle is solved
            path = []
            while current_node:
                path.append(current_node.state)
                current_node = current_node.parent
            return path[::-1]
        neighbors = get_neighbors(current_node.state)
        for neighbor_state in neighbors:
            if tuple(neighbor_state) not in closed_set:
                neighbor_node = PuzzleNode(neighbor_state, current_node, cost=current_node.cost+1)
                heapq.heappush(open_set, neighbor_node)
    return None 
def print_solution(solution):
    if solution:
        print("Solution:")
        for step, state in enumerate(solution):
            print(f"Step {step + 1}:\n")
            for i in range(0, 9, 3):
                print(state[i:i+3])
            print("\n")
    else:
        print("No solution found.")
if name == "main":
    # Example initial state
    initial_state = [1, 2, 3, 4, 5, 6, 8, 7, 0]
    solution = a_star_search(initial_state)
    print_solution(solution)
