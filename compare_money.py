def low_money(cost, given):
    if cost > given:
        a = cost - given
        print("Sorry that's not enough money. Money Refunded!")

def high_money(cost, given):
    if cost < given:
        b = given - cost
        print(f"Please collect your change of ₹{b}")



