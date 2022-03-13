#there are several data types in python , the type() function returns the type of a value 
from typing import SupportsComplex


print(type("hello"))
print(type(12.3))
print(type(23))
print(type(True))

#sometimes we need to change the value from one type to another . this is called type conversion

age = "23"
if int(age) < 25:
    print("you are too young")

#pyhon has build in function of str() , int() , float() , bool() for type conversion of suitable values .
# hence we change float to integer.

size = 23.3
print(int(size)) 

#ANOTHER
score_a = 5
score_b = 4.5
total = score_a + score_b

print(type(score_a))
print(type(score_b))
print(type(total))

#sometimes we need to convert value type

position = 5
#message = "your number" + position + "in the queue"
# it will show error 
message = "your number" + str(position) + "in the queue"
print(message)

#another

price = 9.99
print(int(price))#output = 9

#another
member = True
value = int(member)
print(value) #output = 1 for true and 0 for false

#another
#python also provides the list() , dict() , set() , tuble() for conversion pf suitable compounds data structure
choices = ["pizza" , "kebab", "burger", "pizza"]
unique = set(choices)
print(unique)#set command shows only unique elements in set..

#another
users = dict([('james' , 23), ('sj' , 45) , ("gv " , 67)])
print(users)#dict use for group wise data represenation

#another
