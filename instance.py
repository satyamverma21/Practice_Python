#when we want oto use our class to make something
#we start by creating a variable

class virtual_pet :
    color = "brown"
    leg = 4
    age = 9

tommy = virtual_pet()
toto = virtual_pet()

#-------------------------------------------------------------------------------------------------------------

#too access a class variable , we add the instance name { . }  , name of variable we want..

class virtual_pet :
        color = "brown"
        leg = 4
        age = 9

# we need to define first that this variable belongs to class.
# this also called { instance }

tommy = virtual_pet() # {instance} 
print(tommy.color)
print(tommy.age)
print(tommy.leg)

#-----------------------------------------------------------------------------------------------------------------

