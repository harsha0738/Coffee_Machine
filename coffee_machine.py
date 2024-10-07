from data import MENU, resources
from compare_money import low_money, high_money


# print(MENU)
# print(resources)

"""global variable money which stores the profit of the drinks."""
money = 0


water = resources["water"]
milk = resources["milk"]
coffee = resources["coffee"]
"""print all the resources available."""
# print(f"Resources : {water}, {milk}, {coffee}")



water_espresso = MENU["espresso"]["ingredients"]["water"]
milk_espresso = MENU["espresso"]["ingredients"]["milk"]
coffee_espresso = MENU["espresso"]["ingredients"]["coffee"]
money_espresso = MENU["espresso"]["cost"]
"""prints the resources of espresso and its cost."""
# print(f"Espresso : {water_espresso}, {milk_espresso}, {coffee_espresso}, {money_espresso}")

water_latte = MENU["latte"]["ingredients"]["water"]
milk_latte = MENU["latte"]["ingredients"]["milk"]
coffee_latte = MENU["latte"]["ingredients"]["coffee"]
money_latte = MENU["latte"]["cost"]
"""prints the resources of latte and its cost."""
# print(f"Latte :{water_latte}, {milk_latte}, {coffee_latte}, {money_latte}")

water_cappuccino = MENU["cappuccino"]["ingredients"]["water"]
milk_cappuccino = MENU["cappuccino"]["ingredients"]["milk"]
coffee_cappuccino = MENU["cappuccino"]["ingredients"]["coffee"]
money_cappuccino = MENU["cappuccino"]["cost"]
"""prints the resources of cppuccino and provides its cost."""
# print(f"Cappuccino : {water_cappuccino}, {milk_cappuccino}, {coffee_cappuccino}, {money_cappuccino}")

"""espresso function"""
def espresso():
    global water, milk, coffee, money
    if water > water_espresso:
        # print("sufficient water")
        water = water - water_espresso
        if milk > milk_espresso:
            # print("sufficient milk")
            milk = milk - milk_espresso
            if coffee > coffee_espresso:
                # print("sufficient coffee")
                coffee = coffee - coffee_espresso
                money = money + MENU["espresso"]["cost"]
                # print(money)
                print("here is your drink")

                """prints the available resources."""
                # print(f"Resources : water :{water}, milk : {milk}, coffee : {coffee}, money : {money}.")
            else:
                print("Sorry! You can't have the drink bcoz of in sufficient coffee.")
        else:
            print("Sorry! You can't have the drink bcoz of in sufficient milk.")
    else:
        print("Sorry! You can't have the drink bcoz of in sufficient water.")

"""latte function"""
def latte():
    global water, milk, coffee, money
    if water > water_latte:
        # print("sufficient water")
        water = water - water_latte
        if milk > milk_latte:
            # print("sufficient milk")
            milk = milk - milk_latte
            if coffee > coffee_latte:
                # print("sufficient coffee")
                coffee = coffee - coffee_latte
                money = money + MENU["latte"]["cost"]
                # print(money)
                print("here is your drink")
                # print(f"Resources : water :{water}, milk : {milk}, coffee : {coffee}, money : {money}.")
            else:
                print("Sorry! You can't have the drink bcoz of in sufficient coffee.")
        else:
            print("Sorry! You can't have the drink bcoz of in sufficient milk.")
    else:
        print("Sorry! You can't have the drink bcoz of insufficient water ")

"""cappuccino function"""
def cappuccino():
    global water, milk, coffee, money
    if water > water_cappuccino:
        # print("sufficient water.")
        water = water - water_cappuccino
        if milk > milk_cappuccino:
            # print("sufficient milk")
            milk = milk - milk_cappuccino
            if coffee > coffee_cappuccino:
                # print("sufficient coffee")
                coffee = coffee - coffee_cappuccino
                money = money + MENU["cappuccino"]["cost"]
                # print(money)
                print("here is your drink")
                # print(f"Resources : water :{water}, milk : {milk}, coffee : {coffee}, money : {money}.")
            else:
                print("Sorry! You can't have the drink bcoz of in sufficient water.")
        else:
            print("Sorry! You can't have the drink bcoz of in sufficient milk.")
    else:
        print("Sorry! You can't have the drink bcoz of insufficient water ")


is_on = True

while is_on:
    choice = input("What would you like to have? (espresso/latte/cappuccino) : ")
    # print(choice)
    if choice == "espresso":
        amount = int(input(f"Please Pay {money_espresso} to collect your {choice}.\n"))
        if amount == money_espresso:
            espresso()
        elif amount < money_espresso:
            low_money(money_espresso, amount)
        elif amount > money_espresso:
            espresso()
            high_money(money_espresso, amount)
        else:
            is_on = False
    elif choice == "latte":
        amount = int(input(f"Please Pay {money_latte} to collect your {choice}.\n"))
        if amount == money_latte:
            latte()
        elif amount < money_latte:
            low_money(money_latte, amount)
        elif amount > money_espresso:
            latte()
            high_money(money_latte, amount)
        else:
            is_on = False
    elif choice == "cappuccino":
        amount = int(input(f"Please Pay {money_cappuccino} to collect your {choice}.\n"))
        if amount == money_cappuccino:
            cappuccino()
        elif amount < money_cappuccino:
            low_money(money_cappuccino, amount)
        elif amount > money_cappuccino:
            cappuccino()
            high_money(money_cappuccino, amount)
        else:
            is_on = False
    elif choice == "report":
        print(f"Water  : {water}ml"
              f"\nMilk   : {milk}ml"
              f"\nCoffee : {coffee}g"
              f"\nMoney : ₹{money}")
    elif choice == "off":
        is_on = False
    else:
        print(f"There is no drink with the name {choice}.Please go through the MENU and enter the available items only!")









# print(f"Resources : {water}, {milk}, {coffee}")