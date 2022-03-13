#sometimes functions need dpecific information to help them perform their task . like a function that adds a player name to a team

def greet_ron():
    name = "Ron"
    print(f"Hello , {name}");

greet_ron()

# how would i greet another person ; i wpuld create a new function with similar code 

def greet_sj():
    name = "sj"
    print(f"hello {name}")

greet_sj()

#instead of writing two codes ...

def greet(name):
    print(f"hello {name}")

greet("sy")
greet("it")
greet("fdjh")

#to pass a value to a function, we first add a variable called a parameter inside the parentheses of a function. Here we will pass name
def hii(name):
    print(f"hello { name}")

hii("sj")
hii("shdj")

#another

def lamp_status(power):
    power = True
    print(f"powered on {power}")

lamp_status()     

#another

def display_half(number):
    half = number/2
    print(half)

display_half(10)