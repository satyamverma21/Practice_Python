#As we build programes , we ofter need to create many similarbut distinct objects...'
#Like various different configurations of a computer.....'

computer1_size ="15"
computer1_storage = "1TB"

computer2_size = "13"
computer2_storage = "256GB"

print("computer1 display size: " + computer1_size )
print("computer1 storage space: " + computer1_storage )

print("computer2 display size: " + computer2_size )
print("computer2 storage space: " + computer2_storage )

#____________________________________________________________________________________________________

#...............[to help us group data and functionality , we create a class]..........................
#.......[ a class is a template that we use to create many similar but distinct things ]....................
#.......................[ first latter of a class should be capital ..........................................................]

class Computer :
    def __init__(self , size , storage):
        self.size = size
        self.storage = storage

    def print_specs(self):
        print("Display size: " + self.size)
        print("Storage size: " + self.storage)

low_spec = Computer("13","256GB")
mid_specs = Computer("15","512GB")
high_spec = Computer("17","1TB")       
premium_specs = Computer("20","2TB")

print("low specs computer")
low_spec.print_specs()

print("high specs computer")
high_spec.print_specs()












