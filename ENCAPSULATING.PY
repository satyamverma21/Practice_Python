############################################################################################################################
#          LET'S LEARN  ABOUT DIFFERENT STYLE OF CODING USED BY DEVELOPERS
#              FUNCTIONAL PROGRAMMING AND OBJECT ORIENTED PROGRAMMING (OOP)
#_______________________________________________________________________________________________________________
############################################################################################################
#           DIFFERENT STYLE OF CODING  ARE ALSO KNOWN AS [ PARADIGMS ]
#              A COMMON STYLE IS CALLED [ FUNCTIONAL PROGRAMMING (FP) ]
#___________________________________________________________________________________________________
######################################################################################################################3

# IN FP WE USE A LOT OF FUNCTIONS AND VARIABLES..................

#                                  [  EXAMPLE 1  ]

def get_total(a,b):
    return a+b

num1 = 2
num2 = 4

total = get_total(num1,num2)
print(total)

#                                    [  EXAMPLE 2  ]

class Car:
    mileage = 12000

    def  drive(self, miles):
        self.mileage += miles

tesla = Car()
tesla.drive(200)

print(tesla.mileage)

#                                     [  EXAMPLE 3  ]

class Dog:
    hungry = True

    def eat(self):
        self.hungry = False

toto = Dog()
print(toto.eat())
print(toto.hungry)

#                                      [  EXAMPLE 4  ]

class Piggy:
    value = 0

    def addmoney(self,amount):
        self.value =  self.value +amount

my_piggy = Piggy()
my_piggy.addmoney(200)
print(my_piggy.value)

############################################################################################################
#                                       SET 2
#          { IN (OOP) WE GROUP RELATED DATA & FUNCTION TOGETHER IN THE SAME OBJECT }
#                              IS CALLED [ENCAPSULATION] 
##################################################################################################################

class Dog :
    name = "toto"
    hungry = False

    def eat(self):
        self.hungry == True





















