###############################(how to add a key to dictionary)##################################

ticket = {
"seat no": 25
}
#adding new value
ticket["window"] = 25
ticket["reserve"] = 56
ticket["reserved_people"] = "sajitya"
print(ticket)
#done

#2  way to check weather dict contains a particular key or not
# for checking we use (in) keyword 

personal_data = {
"name" : "sajitya verma",
"telephone" : "7070707070"

} 
has_address = "address" in personal_data
print("name" in personal_data)
print(has_address)

#########################(how to delete element from dict)#########################################

bio = {
"name": "sajitya",
"height": "5.4",
"color": "average",
"weight": "60",
"phone": "3033033030"
}

bio.pop("color")
print(bio)

#first check weather it is exist or not then remove it.......

if "name" in bio:
    bio.pop("name")

print(bio)
