#when we create objects one by one we can we run into the problem of having dublicate codes
#                     DEEMAAG ACCHE SE MAARNA EK BARI M PURA SAMAJH NHI AAYEGA
#---------------\??????????how many greet methods are there????????????/----------------------------------

class Person1:
    name = "sam"
    def greet(self,name):
        print( "hiiiiiii!!!!")

class Person2:
    name = "raja"
    def greet(self,name):
        print( "hiiiiiii!!!!")

class Person3:
    name = "piku"
    def greet(self,name):
        print( "hiiiiiii!!!!")

#------------------------------\ HERE WE USE IMHERITANCE /-------------------------------------------------

class Parent :                  # let him SET A
    def __init__(self):
        self.eye = "green"

class Child (Parent):           # this is set B it is subset of SET A , BECAUSE OF (PARENT)
    def __init__(self):
        super().__init__()
        self.age = 9

sj = Child()
print(sj.eye)
print(sj.age)  #green , 9

#--------------------------------------------------------------------------------------------------------------------

class Greetings:
    def greet(self):
        print("hii")

class Person(Greetings):
    name = "sj"

p = Person()
p.greet()

#---------------------------------------------------------------------------------------------------------------------

class car:                           # have codes for class car only...
    def start_car(self):
        print("starting car")
    
class hybrid(car):                   # have codes for class car and hybrid also...
    def charge(self):
        print("using fuel to charge batteries ")

class electric(car):
    def fuel(self):
        print("no fuel needed")


honda = hybrid()
tesla = electric()

honda.start_car()
tesla.start_car()

tesla.fuel()
honda.charge()

#---------------------------------------[  set 2 ]-------------------------------------------------------------
#classes contain a method called a CONSTRUCTOR 
#that sets the properties of a new object , known as inheritance....
# to make sure bigger class have same properties as smaller one ,
#                         we code {  super().__init__(name,age,examples) }
# in this {super} = parent class/smaller class
#  { __init__ }  = allow us to use functions of parent class like age , name etc.........

class Person :
    def __init__(self,name , age):
        self.name =name
        self.age = age
    def greet(self):
            print("hiii ", self.name)

class Nurse(Person):
    def __init__(self, name, age):
        super().__init__("Nurse " + name, age) #important
    def Intro(self):
        print("hii i am ", self.name)

sam = Person("samarth",25)
raj = Nurse("raja",20)

raj.Intro()
sam.greet()

#---------------------------------------------------------------------------------------------------------------






















