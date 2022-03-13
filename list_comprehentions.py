#------------------------FIRST READ THIS CODE CAREFULLY-------------------------------------------------------------

prices = [10 ,20 ,33,45,66]
halved = []

for price in prices:
    half_price = price/2 
    halved.append(half_price)# WHATEVER THE O-P WILL COME ,IT WILL ADD TO [ halved ] list

print(halved)

##################[ BETTER WAY OF DOING THIS ]  ; [ LIST COMPREHENTION ]########################

prices = [10 ,20 ,33,45,66]
halved = [price/2 for price in prices]

print(halved) # this is [   list comprehention method   ]

#------------------------------------------[  EXAMPLE  ]-------------------------------------------------

flights = ["1111","2222","3333","4444"]
code_a = ["ba" + flight for flight in flights]

print(code_a)

#---------------------------------------[   BOOLEAN   ]-------------------------------------------------------

answer = [True , False, False]
opposite = [ not ans for ans in answer]

print(opposite)

#------------------------------[ TO MAKE A COPY OF ORIGINAL ]-------------------------------------

naam = ["a","b","c","d","e",55,66,True , False]
naam_copy = [name for name in naam]

print(naam_copy)

#----[ counting a particular alphabet in a word ; using { set1.count("element") }  ]-----------------

words = ["apple","aligator","abracabadra","avatar"]
count_a = [word.count("a") for word in words]

print(count_a)

#################################################################################################################

