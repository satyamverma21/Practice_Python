#  classes can have function too known as {methods} when they are inside a class

#-------------------------------------[ * SELF * ]------------------------------------------------------------------------------

#SELF IS A SPECIAL KEYWOARD WE NEED TO USE INSIDE OUR CLASS...
#WE PASS SELF AS THE FIRST PARAMETER TO ALL THE METHOD WE ADD...
#WE USE SELF AS A PARAMETER IN THE CLASS METHODS ...
#SO THAT WE CAN ACCESS THE CLASS VARIABLES INSIDE THE METHOD...


from _typeshed import Self


class virtual_pet:
    color = "brown"

    def bark(self):   #SELF == SO THWT WE CAN ACCESS BARK ...
        print("bark")

toto = virtual_pet()
toto.bark()

#--------------------------------------------------------------------------------------------------------

class virtual_pet:
    color = "brown"
    bark = True
    leg = 4

    def bark(self):   #SELF == SO THAT WE CAN ACCESS BARK ...
        print("bark")

    def display_color(self):
        print(Self.color)     #SELF = TO ACCESS VALUE OF COLOR FROM CLASS...

    def display_leg(self):
        print(self.leg)     #SELF = TO ACCESS VALUE OF LEG FROM CLASS...

toto = virtual_pet()
toto.bark()
toto.display_leg()
toto.display_color()





















