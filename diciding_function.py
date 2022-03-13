def add_shopping(cart):
    if cart < 100:
        print(f"total:{cart + 12}")
    else:
        print(f"total {cart}")

add_shopping(23)
add_shopping(200)

####small code for can drive 

def can_drive(age):
    if age >=18:
        print("yes u can !")

can_drive(19)

####

def get_waiting_list(signups):
    if signups > 200 :
        print(f"waiing list : {signups - 200}")

get_waiting_list(250)


#bjsaddaskdfgadfjsgdfsgflkdfldfasldfadlkfhadlfadldfasdfdfdfkdfkffkhsdfkhdkfhhsdhfhhkfhkhfkh

#we can nest all kinds of conditional inside function luike this else statement

def calculate(operator ,x,y):
    if operator == "+":
        print(x + y)
    elif operator == "-":
        print(x-y)
    else :
        print(f' unknown operator {operator}')
calculate("-",678,67)

################

def show_progress(points):
    if points > 1000:
         print("new highest score")    
    print("next level")

show_progress(900)