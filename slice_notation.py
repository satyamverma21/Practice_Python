####...........sometimes we want to retrieve multiple value from a list........................
####...............we can do the using { //  SLICING  // }..........................................
####...............lets look at the [ START:STOP ] syntax......................................................

items = ["egg","sugar","flour","salt"]
# first value == starting point , another one is stopping point
 
print(items[0:2])    # it will give 0 and 1 ; not 2
print(items[3:])     # it will give only 3 (last value)
print(items[1:])     # it will give 1 , 2 and 3 (till last)
print(items[:])      # show all

print(items[-2:])    # it will count from last but move asusual ; give {-2 and -1} or {2 and 3}
print(items[:2])     # we simply deciding a ending point which starts from 0 to 2(as the respected value)

print(items[2:0])     # this is in opposite direction ; doesn't give error ; give empty list


#==========================[  we can also use [start : stop : step]  ]=====================================================================================

#.............[ step = jump ]

abc = ["a","b","c","d","e","f"]
print(abc[1:6:2]) # b , d , f or 1 , 3 , 5

#..............[step can be negative , which show opposite directional movement of list flow]


abc = ["a","b","c","d","e","f"]

####################################[ THODA DEEMAG MAAR NA PDEGA !!!!!!]

print(abc[2::-1])    #.....['c', 'b', 'a']
print(abc[:3:2])     #.....['a', 'c']
print(abc[3:0:-1])   #.....['d', 'c', 'b']
print(abc[::-3])     #.....['f', 'c']
print(abc[0:2:-1])   #.....[]
print(abc[4:1:-1])   #.....['e', 'd', 'c']







