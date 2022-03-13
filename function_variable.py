#variable creted inside a function have a localscope like bonus here

from typing import final


def add_bonus(salary):
    bonus = 900
    print(salary + bonus)
add_bonus(1100)


#####

def add_bonus(salary):
    bonus = 900
    bonus = 800
    print(salary + bonus)
add_bonus(1100)

####don't update the variable outsides the function block

def apply_discount(price):
    discount = 55
    return price - discount

final_price = apply_discount(555)
print(final_price)

######lkrtjrfgafqfhqfhifhqiehfkjhfhqifiafhbwekfqksfdhskjdhfkhekfhsdhfihifnhfhiehih

#variable created outside of a function block have a global scope like dhiping here''''

shipping = 90
def calculate_total(cart):
    print(cart + shipping)

calculate_total(90)

#########

single_payer = True

if single_payer:
    player_1 = "mario"

print(f"player 1 : {player_1}")

##########

rent = 1000
def calculate_spending(groceries):
    print(f"total {rent + groceries}")

print(f"rent {rent}")
calculate_spending(300)

########## use of i in range , bataya hi nhi

price = 100

for i in range(20):
    discount = 10
    discount += 1 
    price = price - discount
    print(price)

print(f"discount : {discount}")
