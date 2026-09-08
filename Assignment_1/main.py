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



def load_maze(JSON_file):
    pass

def build_maze():
    pass

def bfs(graph, start, goal):

def dfs(graph, start, goal):


def main():
    items = [Item("Bread", 5, 6), Item("Milk", 4, 7), Item("Eggs", 6, 8), Item("Chocolate", 8, 9)]
    reflex_agent(20, items)
    utility_agent(20, items)

if __name__ == "__main__":
    main()