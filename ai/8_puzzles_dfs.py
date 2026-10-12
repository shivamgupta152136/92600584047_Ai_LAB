def get_neighbours (state):
    neighbours=[]
    zero_index=state.index(0)
    row,col=divmod(zero_index,3)
    moves=[(-1,0),(1,0),(0,-1),(0,1)] #up,down,left,right
    for move in moves:
        new_row,new_col=row+move[0],col+move[1]
        if 0<=new_row<3 and 0<=new_col<3:
            new_index=new_row*3+new_col
            new_state=list(state)
            new_state[zero_index],new_state[new_index]=new_state[new_index],new_state[zero_index]
            neighbours.append(tuple(new_state))
    return neighbours
def print_path(path):
    for state in path:
        for i in range(0,9,3):
            print(state[i:i+3])
def dfs(state,goal):
    stack=[state]
    visited=set()
    parent={state: None}
    while stack:
        current=stack.pop()
        if current==goal:
            path=[]
            while current is not None:
                path.append(current)
                current=parent[current]
            return path[::-1]
        visited.add(current)
        for neighbour in get_neighbours(current):
            if neighbour not in visited and neighbour not in stack:
                stack.append(neighbour)
                parent[neighbour]=current
    return None
state=(
    1,2,3,
    4,0,5,
    7,8,6,
)

goal=(
    1,2,3,
    4,5,6,
    7,8,0,
)
path=dfs(state,goal)
print_path(path)