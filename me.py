X = 1
Y = 1
Z = 2
N = 3
lis = [[x, y, z] for x in range(X+1) for y in range(Y+1) for z in range(Z+1) if x + y + z != N]
print(lis)