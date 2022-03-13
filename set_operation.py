#get length of list
frnds ={"emma","watson","lilly","harry","potter","ron"}
print(frnds,len(frnds))

###SUBSET

frnds ={"emma","watson","lilly","harry","potter","ron"}
chat ={"harry","potter","ron"}  #it is subset of frnds..........

print(chat.issubset(frnds))  #way to check................



#............................................{ 2 }...........................................................


#add two sets...............{   set1.union(set2)   }
chat ={"harry","potter","ron"} 
frnds ={"emma","watson","lilly"}

print(chat.union(frnds))

#finding common between two sets..............{    set1.intersection(set2)   }

classA = {"a","b","c","d"}
classB ={"a","d","e"}

print(classA.intersection(classB))

#to get uncommon/different/difference between 2 sets ...........{  set1.difference(set2)   }

classA = {"a","b","c","d"}
classB ={"a","d","c"}

print(classA.difference(classB))

#####################################################[set1 : primary set ]
#####################################################[set2 : secondary set]

#//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
