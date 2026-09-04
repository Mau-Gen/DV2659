class Item():
    def __init__(self, n: str, p: int, s: int):
        self.name = n
        self.price = p
        self.satisfaction = s

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
    print(f"The total satisfaction of the basket is {total_s}.")

def utility_agent(budget, items):
    basket = []
    amount = 0
    total_s = 0

def main():
    items = [Item("Bread", 5, 6), Item("Milk", 4, 7), Item("Eggs", 6, 8), Item("Chocolate", 8, 9)]
    reflex_agent(20, items)

if __name__ == "__main__":
    main()