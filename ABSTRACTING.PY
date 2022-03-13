#lets try a model a complicated object , like a car using OOP ...........
#when we drive a car , we don't need to understand inner mechanics of car..................

#similarly , when we working on a code we want to understand the core methods without being bogged down by details..

# a car inject and ignite fuel thousand of times in a minute......

class Car:
    def inject_fuel(self):
        print("spreying fuel")
    def ignite_fuel(self):
        print("boom!!!")

toyota = Car()
toyota.inject_fuel()
toyota.ignite_fuel()
toyota.inject_fuel()
toyota.ignite_fuel()
toyota.inject_fuel()
toyota.ignite_fuel() #this is how a car works...........through coding

#_______________________________________________________________________________________________________
#--------------------------------[ INTERESTING ]----------------------------------------------------
#***************************************************************************************************

# However , repeatedly calling method can make it harder to read and use........
# cars do all of this low level functionality for for us........
# we only had to start the car .....
# hiding these details is called [  ABSTRACTION  ]
# we implement abstraction in OOP by  writing few core functions that handle all of the low level work


class Car:
    def __init__(self):
        self.on = False

    def inject_fuel(self):
        print("spreying fuel")
    def ignite_fuel(self):
        print("boom!!!")

    def startup(self):
        self.on = True
        while self.on:
            self.inject_fuel()
            self.ignite_fuel()


tar = Car()
tar.startup()


#-------------------------------------------------------------------------------------------------------



















