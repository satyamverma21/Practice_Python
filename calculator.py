#let's uses our knowledge of if elif and else statement to code a shipping cost calculator.

# we will save destination type and total purchase cost in variables , then we will update the shipping cost based on the destination.
international_shipping = True

total = 150
shipping_cost = 0

if international_shipping:
    shipping_cost += 15
    print("international charges applied")
         
if total <= 50:
    shipping_cost += 20
    
elif total <= 100 :
    shipping_cost += 15

else:
    shipping_cost +=  5

print(f"shipping cost : {shipping_cost}")