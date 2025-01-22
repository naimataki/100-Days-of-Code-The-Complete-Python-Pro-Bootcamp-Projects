MENU = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffee': 18,
        },
        'cost': 1.5,        
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffee': 24,
        },
        'cost': 2.5,
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffee': 24,
        },
        'cost': 3.0,
        },
}

profit = 0

resources = {
    'water': 300,
    'milk': 200,
    'coffee': 100,
}

def is_resource_sufficient(order_ingredients):
    '''Returns True when order can be made, False when not enough ingredients.'''
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True

def process_coins():
    print("Please insert coins.")
    total = int(input("How many quarters?:")) * 0.25
    total += int(input("How many dimes?:")) * 0.10
    total += int(input("How many nickels?:")) * 0.05
    total += int(input("How many pennies?:")) * 0.01
    return total

def is_transaction_successful(payment, drink_cost):
    if payment < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(payment - drink_cost, 2)
        global profit
        profit += drink_cost
        print(f"Here is ${change} in change")
        return True
    
def make_coffee(drink, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink} ☕️. Enjoy!")

is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == 'off':
        is_on = False
    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
