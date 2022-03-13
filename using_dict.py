#we access dict. value  by their key ,like here with name

actor_bio = {
"name" : "kartik",
"known for" : ["LOST IN WOODS" , "rushmore" ]
}
actor_name =actor_bio["name"]
print(actor_name)

#we can loop through the keys of dict

player_score = {
"a": 4,
"b": 5,
"c" : 6,
"d": 7
}

for player in player_score:
    print(player_score[player])


# after accessing the value we can update it like any other variable by = followed by new value

ticket = {
"seat no" : 25,
"first class" : False
}
ticket["seat no"] =666 
print(ticket)

#$#####


win_score = {
"1st" : ("ted", 50),
"2nd" : ("gopi" , 60)

}
for win in win_score:
    print(win_score[win])

#fdksdfvnkwjlriri

air = {
"nitrogen": "78%",
"oxygen": "21%",
"argon": "0.93",
"co2": "0.04",
"other":"0.03"
}
print(air["argon"])