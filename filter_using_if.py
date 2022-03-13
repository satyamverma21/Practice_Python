#----------------------[  we can add if condition to filter the new list  ]----------------------------


scores = [32,13,58,43,54,38]
score_above_20 = [ score for score in scores if score>40]

print(score_above_20)


#--------------------------------[  another example  ]------------------------------------------

websites = ["nytimes.com","lemonade.fr","economist.com" ]
french = [ web for web in websites if web.count("a")> 0]

print(french)

#___________________________________________________________________________________________________________________________________-
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
