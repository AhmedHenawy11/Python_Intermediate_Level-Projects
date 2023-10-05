from Data import menu, profit, resources


def espresso(d, w, c):
    price = menu["espresso"]["cost"]
    if price > d:
        return "Sorry that's not enough money. Money refunded."
    elif w < 50:
        return "Not enough water!"
    elif c < 18:
        return "Not enough coffee!"
    elif price < d:
        reminder = d - price
    return f"Here is your espresso ☕️. Enjoy!\nHere is ${reminder} in change."


def latte(d, w, m, c):
    price = menu["latte"]["cost"]
    if price > d:
        return "Sorry that's not enough money. Money refunded."
    elif w < 200:
        return "Not enough water!"
    elif c < 24:
        return "Not enough coffee!"
    elif m < 150:
        return "Not enough milk!"
    elif price < d:
        reminder = d - price
    return f"Here is your latte ☕️. Enjoy!\nHere is ${reminder} in change."


def cappuccino(d, w, m, c):
    price = menu["cappuccino"]["cost"]
    if price > d:
        return "Sorry that's not enough money. Money refunded."
    elif w < 250:
        return "Not enough water!"
    elif c < 24:
        return "Not enough coffee!"
    elif m < 100:
        return "Not enough milk!"
    elif price < d:
        reminder = d - price
    return f"Here is your cappuccino ☕️. Enjoy!\nHere is ${reminder} in change."


def report(w, m, c, p):
    print("the current resource values. e.g.")
    print(f"Water: {w}m\nMilk: {m}ml\nCoffee: {c}g\nProfit: ${p}")


def start():

    off = False
    water = 1500
    milk = 900
    coffee = 500
    profit = 0
    dollars = 0

    choice = input("What would you like? (espresso/latte/cappuccino): ")

    while not off:

        if off == True or choice == "off":
            return 0

        if choice == "espresso":
            dollars = int(input("Please insert dollars$.\n"))
            print(espresso(dollars, water, coffee))
            water -= 50
            coffee -= 18
            profit += 5.5
        elif choice == "latte":
            dollars = int(input("Please insert dollars$.\n"))
            print(latte(dollars, water, milk, coffee))
            water -= 200
            milk -= 150
            coffee -= 24
            profit += 7.5
        elif choice == "cappuccino":
            dollars = int(input("Please insert dollars$.\n"))
            print(cappuccino(dollars, water, milk, coffee))
            water -= 250
            milk -= 100
            coffee -= 24
            profit += 9
        elif choice == "report":
            report(water, milk, coffee, profit)
        else:
            off = True

        choice = input("What would you like? (espresso/latte/cappuccino): ")


start()
