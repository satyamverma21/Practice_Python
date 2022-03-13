#any type of value can serve  as a function input or output. lets look at how functions can make use of lists like players
def is_multiplayer(players):
    print(len(players) == 2)

players = ["ary" , "jay"]
is_multiplayer(players)

#we pass lists  to functions just like we do any other by coding a list name like movie_list between the functions parantheses

def display_programme(movies):
    print(f"airing tonight : ")
    print(movies)
movie_list=["alien", "moon"]
display_programme(movie_list)

#333
def is_booked(pessengers):
    print(len(pessengers)>4)

pessengers = ["sam", "gov", "june"]
is_booked(pessengers)

##

def game_winner(top_player):
    winner= top_player[0]
    print(f"game winner: {winner}")

top_player = ["a","b","c"]
game_winner(top_player)

##  
def update_first_place(leaderboard,player):
    leaderboard[0]= player
    return leaderboard

leaderboard=["a","b","c","d"]
leaderboard=update_first_place(leaderboard,"lenA")

print(leaderboard)