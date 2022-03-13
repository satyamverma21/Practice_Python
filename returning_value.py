#A function can return a value to the code  that called it .
# this program returns a value to the code that it to help perform its task.

def age_lebel(age):
    label ="user age " + age 
    return label

print(age_lebel("22"))
#instead of writing print label we use erturn label

#another
def age_record(age):
    label = "user age : " + age
    return label

result = age_record("34")
result2 = age_record("45")
print(result)
#if we don't iclude a return statement the fuction return none


def give_me_ten():
    return 10
print (give_me_ten)

# another 

def add_greeting(user):
    greeting = "greetings  "+ user
    return greeting 

result = add_greeting("sj")
print(result)

#return a single value from this function

def half_twice(num):
    half  = num/2
    half_again = half / 2
    return half_again
result = half_twice(12)
print(result)

#another

def add_ten(num):
    sum = 10 + num
    return sum

print(add_ten(23))