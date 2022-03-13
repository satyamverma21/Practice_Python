#it actually tells us about how often a element repeat in given list or data sets
answers = ["yes" , "no ", "sometimes" , "yes" , "no"]
#to count answer.count()
print( answers.count("yes"))

#for boolean
free_seats = [False,False,True,False,True]
free = free_seats.count(False)
print(free)

# if we don't want to know the exact number but only if an element like "sugar " exist we use the (in) keyword
shopping = ["flore","eggs","sugar","butter"]
has_eggs = "eggs" in shopping
print(has_eggs) # output= true 
print("niock" in shopping) #output = false

#numbers 

winning = [2,3,4,5,6,5]
print(2 in winning)