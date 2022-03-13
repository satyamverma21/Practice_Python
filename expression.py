#   IN THIS WE ALREADY DEFINE A FUNCTION TO USE IT LATER IN MAKING OF ANOTHER LIST

# LIKE HERE I USE {  def halve(num)  }---------------#
# AND USE IT LATER IN HALVED LIST----------------#
prices = [12,25,44,78,89,65]

def halve(num):
    return num/2

halved = [halve(price) for price in prices ]

print(halved)

#---------------------------------[ ANOTHER INTERESTING EXAMPLE ]----------------------------------

amt = [10,22,30,40,58,60,200 ]

def half(num):
    no_tax = num*0.85
    return no_tax/2

result = [ half(amount) for amount in amt]

print(result)               #o-p ===== [4.25, 9.35, 12.75, 17.0, 24.65, 25.5, 85.0]


#--------------------------[ reminder : we use .split() for splitting...]----------------------------------------------------------
#_________________________________for a quick revision only________________________________________

author = [ "satyam verma " , "jatin gupta"]

def add_coma(name):
    parts = name.split(" ")
    return parts[0] + "----" + parts[1]

update = [ add_coma(name) for name in author]
print(update)

#___________________________________________________________________________________________________________________________________________________________________________-
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!








