k = input()
arr = input().split()
hashmap = dict()

for num in arr:
    if num in hashmap.keys():
        hashmap[num] += 1 #increment counter
    else:
        hashmap[num] = 1 #add it
     

for key,value in hashmap.items():
    if int(value) != int(k):
        print(key)