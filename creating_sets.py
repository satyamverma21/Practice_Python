# when we want to make surea that a collection of value can't havae any duplicate , we store in a set ,

postcodes ={"sw1a" ,"sy3", "b44" }
print(postcodes)
#sets = shows unique value only

#/////////////////////////////////////(using sets)/////////////////////////////////////////////////

#[] use for list , {} use for sets

##################################(how add a new value to a set)###################################################

#we use {   .add()   }

answer ={ "yes ", "no"}
answer.add("maybe")
print(answer)

######print particular value

print(answer[0])

#####

answer_options = {"yes "," no "}

for  answer in answer_options:
    print(f"option : {answer}")

########to remove a set we use {  .remove()   }
subjects = {"geo", "math", "english"}

subjects.remove("math")
print(subjects)

#better way is to check first
if "geo" in subjects:
    subjects.remove("geo")
print(subjects)

###############################(we can convert a list into set to avoid repeatation of elements)

names = { "sa" , "ty" , "am", "sa" , "ji" , "tya"}
print(set(names))

###########################################################################################################################################################################################################################z