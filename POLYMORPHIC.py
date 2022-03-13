# WITH INHERITANCE WE CAN EXTEND A CHILD CLASSS 

#----------------------------------------[    PROBLEM    ]----------------------------------------------------------------

class Feline:
    def speak(self):
        print("meow")

class Cat(Feline):
    def lick(self):
        print("licking paw")

class Lion(Feline): # BUT WHAT IF WE WANT TO IMPLEMENT CHILD BEHAVIOURS DIFFERENTLY FROM EACH OTHER....
    def pray(self):
        print("prounce on pray")


cat = Cat()
cat.speak()   #meow

lion = Lion()
lion.speak()  #meow , but this is wrong lion is meowing...

#-------------------------------------------[   IT'S SOLUTION  ]-------------------------------------------------------

#  WE WANT DIFFERENT BEHAVIOUR OF speak() BASED ON THIS CLASS
#  A SUBCLASS CAN OVERRIDE THE METHOD , SIMPLY SET A SUB CLASS WITH SAME NAME

class Feline:
    def speak(self):
        print("meow")

class Cat(Feline):
    def lick(self):
        print("licking paw")

class Lion(Feline): 
    def pray(self):
        print("prounce on pray")
    def speak(self):
        print("roar")


cat = Cat()
cat.speak()

lion = Lion()
lion.speak()  




