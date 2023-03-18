a = input()
a = {int(i) for i in a.split()}

n = int(input())

strict_superset = True
for i in range(n):
    other_set = input()
    other_set = {int(j) for j in other_set.split()}
    
    if a.issuperset(other_set)==False:
        strict_superset = False
        
print(strict_superset)