###############[  python allows to use negative indexing to get value from last  ]#################################

scores = [4.5,9,1,6.5]
latest = scores[-1]
#-----------------------(  with negative sign now it will count from last )----------------------
print(latest)

#____________________________[  TUPLE does not support value reassign  ]_______________________

info = ("a","b","c","d")
info[-4] = "G"

print(info[0])# it will give ERROR ; () = tuple , [] = list , {} = set.............


#_________________________[   DELITION :- WE USE { del } funtion to delete  ]_______________________________________________________

num = ["22","90","33","55"]
del num[-1],num[0]

print(num)


#.......................................another example............................................

product = {
"category": "book",
"price": 4.99,
"in_shop":True
}

del product["in_shop"]
print(product)

#___________________________________________________________________________________________________________________________



