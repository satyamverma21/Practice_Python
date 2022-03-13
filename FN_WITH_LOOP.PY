from typing import Counter


def onboard_pessenger(booking):
    counter =1
    while counter <=booking:
        print(f"pessenger {counter} on board")
        counter += 1
onboard_pessenger(10)
##

def display_downloading(total_files):
    for i in range(total_files):
        print(f"downloading file {i} out of {total_files}")

display_downloading(8)
##

def do_countdown(counter):
    while counter > 0 :
        print(counter)
        counter -= 1
    print("go")

do_countdown(5)
##

def half_prices(cart):
    for price in cart :
        print(f"new price {price/2}")

cart_list =[23,34,45]
half_prices(cart_list)

##

def show_next_track():
    playlist =["song 1","song 2","song 3 ","song 4","song 5"]
    for track in playlist:
        print(f"coming next {track}")

show_next_track()
