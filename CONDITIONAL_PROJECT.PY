from typing import final


ride_type = "black"
credits =4

ride_price = 0
final_price = 0 

if ride_type == "white":
    ride_price = 20
elif ride_type == "black":
    ride_price = 15
else:
    ride_price = 25

print("ride price :")
print(ride_price)

if credits > 0 :
    final_price = ride_price - credits

print("final price : ")
print(final_price)

