#appent = bs value enter kro
#insert  = cordinates ke sath value enter kro
#pop() = to remove the last element
# pop(element number) = to remove the specified number 
#we can run popp command even after store it into a variable

#lets learn how to add or remove values in a list . Like in this app, which uses a list to manage user's score data.
## to add a the value to a list .we can code the list name followed by a period ( . ) .
# then the instruction append(value)

score = [ 22 ,23 ,24 , 25]
score.append(99)
score.append(5348)
score.append(987)
score.append(8487)
#this is how class.append work in adding a new value in existing class

print(score)
#we can insert a value in specific index with {"class.insert(it's position" , "string" )}.

shopping = ["apple ", "mango" ]
shopping.insert(0,"grapes")
print(shopping)

#to remove the last element of a list ,we code the list name (todo) a period . and the instruction pop().


# the removed value can be store in a variable too . EXAMPLE.........
todo = ["eat","bath","sleep"]

removed = todo.pop(2) 
print(todo)
print(removed + " REMOVED")
#OK we can run the pop command even after store it into a variable

sj = [3 , 4 ,5,6,7,8]
sj.append(32)
sj.append(40)
sj.insert(5 , 5456)
sj.insert(6 , 999)
sj.pop(8)
sj.pop(2)
print(sj)