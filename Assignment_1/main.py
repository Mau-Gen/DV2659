from itertools import combinations
import json

class Item():
    def __init__(self, n: str, p: int, s: int):
        self.name = n
        self.price = p
        self.satisfaction = s
    def __repr__(self):
        return "[{},{},{}]".format(self.name, str(self.price), str(self.satisfaction))

class Combination():
    def __init__(self, l: list, p: int, s: int):
        self.list = l
        self.total_price = p
        self.total_satisfaction = s
    def __repr__(self):
        return "[{},{},{}]".format(self.list, str(self.total_price), str(self.total_satisfaction))

def reflex_agent(budget, items):
    basket = []
    amount = 0
    total_s = 0
    for item in items:
        if amount + item.price <= budget:
            if item.price <= 5:
                basket.append(item)
                amount += item.price
                total_s += item.satisfaction
            elif item.satisfaction > 8:
                basket.append(item)
                amount += item.price
                total_s += item.satisfaction
      
    print("The basket contains these items as according to the reflex bot:\n")
    for item in basket:
        print(f"{item.name, item.price, item.satisfaction}\n")

    print(f"The total price of the basket is {amount}.\n")
    print(f"The total satisfaction of the basket is {total_s}.\n")

def utility_agent(budget, items):
    combs = []

    for i in range(1, len(items)+1):
        for r in combinations(items, i):
            comb_price = sum(item.price for item in r)
            comb_satisfaction = sum(item.satisfaction for item in r)
            if comb_price <= budget:
                combs.append(Combination(r, comb_price, comb_satisfaction))
    print(f"These are all the combinations that are possible for the budget:\n\n{combs}\n")
    best_comb = max(combs, key=lambda comb: (comb.total_satisfaction, -comb.total_price))

    return print(f"This is the best possible combination for satisfaction:\n{best_comb} \nThe total satisfaction is: {best_comb.total_satisfaction}")

def get_neighbors(graph, vertex):
    row, col = vertex
    neighbors = []

    directions = [
        (1,0), 
        (-1,0), 
        (0,1), 
        (0,-1)
    ]

    for dr, dc in directions:
        new_row = row + dr
        new_col = col + dc

        if 0 <= new_row < len(graph) and 0 <= new_col < len(graph[0]):
            if graph[new_row][new_col] == 0:
                neighbors.append((new_row, new_col))

    return neighbors



def from_json(JSON_file):

    with open(f"{JSON_file}", "r") as file:
        data = json.load(file)

    return data
        

def to_json(item, name):
    with open(f"{name}.json", "w") as file:
        json.dump(item, file)


def bfs(graph, start, goal, filename):

    visited = {start}

    queue = [start]

    parent = {}

    solved_maze = [row[:] for row in graph]

    found = False

    while queue:

        curr = queue.pop(0)

        if curr == goal:
            found = True
            break

        neighbors = get_neighbors(graph, curr)

        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = curr
                    visited.add(neighbor)
                    queue.append(neighbor)

    
    
    if not found:
            print("No path found!")
            return
    
    path = []

    curr = goal

    while curr != start:
        path.append(curr)
        curr = parent[curr]

    path.append(start)

    path.reverse()

    for row, col in path:

        if (row, col) == start:
            solved_maze[row][col] = "S"

        elif (row, col) == goal:
            solved_maze[row][col] = "G"

        else:
            solved_maze[row][col] = "*"

    data = {
            "start": start,
            "goal": goal,
            "steps": len(path) - 1,
            "path": path,
            "maze": solved_maze
        }
    
    to_json(data, filename)
    return

    

def dfs(graph, start, goal, filename):

    visited = set()

    stack = [start]

    parent = {}

    solved_maze = [row[:] for row in graph]

    found = False

    while stack:
        curr = stack.pop()

        if curr in visited:
            continue

        visited.add(curr)

        if curr == goal:
            found = True
            break
            
        neighbors = get_neighbors(graph, curr)
        if neighbors:
            for neighbor in neighbors:
                if neighbor not in visited:
                    if neighbor not in parent:
                        parent[neighbor] = curr
                    stack.append(neighbor)

    if not found:
        print("No path found!")
        return

    path = []

    curr = goal

    while curr != start:
        path.append(curr)
        curr = parent[curr]

    path.append(start)

    path.reverse()

    for row, col in path:

        if (row, col) == start:
            solved_maze[row][col] = "S"

        elif (row, col) == goal:
            solved_maze[row][col] = "G"

        else:
            solved_maze[row][col] = "*"

    data = {
            "start": start,
            "goal": goal,
            "steps": len(path) - 1,
            "path": path,
            "maze": solved_maze
        }
    
    to_json(data, filename)
    return



def main():
    items = [Item("Bread", 5, 6), Item("Milk", 4, 7), Item("Eggs", 6, 8), Item("Chocolate", 8, 9)]
    reflex_agent(20, items)
    utility_agent(20, items)

    data = from_json("graph.json")

    maze = data["maze"]

    s = tuple(data["start"])

    g = tuple(data["end"])

    bfs(maze, s, g, "bfs_solved")

    data = from_json("bfs_solved.json")

    bfs_solved = data["maze"]

    bfs_steps = data["steps"]

    bfs_string = ""

    for i, _ in enumerate(bfs_solved):
        for j, _ in enumerate(bfs_solved[i]):
            bfs_string += str(bfs_solved[i][j])
            bfs_string += " "
        bfs_string += "\n"

    print(bfs_string)
    print(f"Total amount of steps taken with BFS: {bfs_steps}\n")

    dfs(maze, s, g, "dfs_solved")

    data = from_json("dfs_solved.json")

    dfs_solved = data["maze"]

    dfs_steps = data["steps"]

    dfs_string = ""

    for i, _ in enumerate(dfs_solved):
        for j, _ in enumerate(dfs_solved[i]):
            dfs_string += str(dfs_solved[i][j])
            dfs_string += " "
        dfs_string += "\n"

    print(dfs_string)

    print(f"Total amount of steps taken with DFS: {dfs_steps}\n")

if __name__ == "__main__":
    main()