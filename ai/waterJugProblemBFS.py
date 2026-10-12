#water jug problem

#capacity of two jug
cap_a = 4
cap_b = 3

#goal amount
goal = 2

# function to print the state

def print_state(state):
    print("Jug A:", state[0],"litres")
    print("Jug B:", state[1],"litres")
    print()

#genrate all possible moves
def get_neighbors(state):
    neighbors = []

    a, b = state

    #1.fill jug A
    if a < cap_a:
        neighbors.append(((cap_a, b),"fill Jug A"))

    #2.fill jug B
    if b < cap_b:
        neighbors.append(((a, cap_b),"fill Jug B"))

    #3.Empty Jug A
    if a > 0:
        neighbors.append(((0, b),"Empty jug a"))

    #4.Empty Jug B
    if b > 0:
        neighbors.append(((a, 0),"Empty jug b"))

    #5.pour jug a->jug b
    amount = min(a, cap_b - b)

    if amount > 0:
        neighbors.append(
                ((a - amount, b + amount),
                    "pour jug a -> jug b")
        )

    #6.pour jug b->jug a
    amount = min(b, cap_a - a)

    if amount > 0:
        neighbors.append(
                ((a + amount, b - amount),
                    "pour jug b -> jug a")
        )

    return neighbors

#BFS Algorithm
def bfs(start):
    queue = [(start,[])]
    visited = set()

    while queue:
        state, path = queue.pop(0)

        if state in visited:
            continue
        
        visited.add(state)

        #check goal
        if state[0] == goal or state[1] == goal:
            return path + [(state,"goal reached")]

        #genrate neighbors
        for neighbor, action in get_neighbors(state):

            if neighbor not in visited:
                queue.append(
                    (neighbor, path + [(neighbor, action)])
                )

    return None

#starting state
start = (0,0)

#run bfs
solution = bfs(start)

#print solution
if solution:

    print("solution found in", len(solution) - 1, "moves:\n")

    print("initial state:")
    print_state(start)

    for state, action in solution:
        print(action)
        print_state(state)

else:
    print("no solution found.")
