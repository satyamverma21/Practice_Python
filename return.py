def get_score_data(score_list):
    highest_scr = max(score_list)
    lowest_scr = min(score_list)
    return highest_scr ,lowest_scr

score = [32,55,67,78,64,34]
data = get_score_data(score)
print(data)
highest = data[0]
lowest = data[1]
print("smallest score ", lowest)
print("highest score ",highest)

#####

def get_top_three(player):
    return player[0] ,player[1], player[2]

players = ["sue ", "ed","ANN","tyy"]
top_three = get_top_three(players)
print("first player", top_three[0])
print("second player", top_three[1])
print("third player", top_three[2])

######

def form_team(players):
    team = []
    team.append(players[0])
    team.append(players[2])
    return team

players = ["sue ", "ed","ANN","tyy"]
team = form_team(players)
team[0] = "satyam"
print(team)

#####

def check_age(age):
    can_drive = age >=18
    return age , can_drive

age = int(input("enter age ''''''::::"))
print(check_age(age))


######

def analyze_profit(gains , expenses):
    profit = gains - expenses
    after_tax = 0.85 * profit
    above_mean = profit > 1000
    return profit , after_tax , above_mean

insights = analyze_profit(3000,1200)
print(f"profit:{insights[0]}")
print(f"above mean : {insights[2]}")

 