def final_price(price , tax):
    return price + tax

price = final_price(45 , 67)
print(price)

#boolean

def is_freezing(temp):
    return temp < 0

freezing = is_freezing(-3)
print(freezing)
#return value might stsart with compute calculate get
#return value might start with is has can
#make sure your function start with  verb
def generate_username(name , birthday ):
    return(f"{name}_{birthday}")

user = generate_username("ty", 45)
print(user)

#another
def getfreeseats(booked , total):
    return total - booked

free = getfreeseats(34,45)
print(free)


#ldfjjgjrdisatya,mjmsatayammmmmmmjmmmmmn;;mn;mjn;dan;an;amen;amn;nnnnamenamenamnmnmanbnmbartbanam

#a function is like black box because black box because when it has a descriptive name ;
#we can call it withoutwithout reading the code inside it 
#it shopwa that we should
# author = "sj verma "
#title = "harry potter"
#year = 1313
#display_year(year)
#display_author(author)

#display_title()
#display_author()
#display_year()

#######

def display_score(name,points):
    print(f" {name}:{points}points")
display_score("sj",34)

#######

def sum_score(score , bonus):
    print(score + bonus)
sum_score(233,446)

#######

def is_old_age(age):
    print(age >= 25)
is_old_age(25)

########

def is_old_age(age):
    return age >= 25

can_drive = is_old_age(25)
print(can_drive)

########

