#we can use different instances from a class more flexible , CALLED [ CONSTRUCTOR ]

#------------------------------------[  __init__  ]--------------------------------------------------
# it is called as constructor method............
# allow us to SET UNIQUE VALUES for the class variables when we createn an INSTANCE.........

class pet:
    def __init__(self,color):
        self.color = color

toto = pet("brown")
bunny = pet("white")
jojo = pet("GREEN")

print(toto.color , bunny.color ,jojo.color)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

class animal :
    def __init__(self, color , name , leg ,height):
        self.color = color
        self.name = name
        self.leg = leg
        self.height = height
        self.all = color , name , leg , height

human = animal("BROWN" , "satyam" , 2 ,5.4)
print(human.all)
print(human.height)

#,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,



        