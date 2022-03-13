print("this is how we get output wheather answer is wrong or right and if answer is == or answer is !=")
answer = "Delhi"
if answer == "Delhi":
    print(answer  + "is correct")
    
answer = "New Delhi"
if answer != "Delhi":
    print(answer +" is wrong!")
     
print("now we will see if answer is <= or >= // and i use string formatting for fun "   )

age = 75
if age >= 55:
    print(f"your age is  {age} discont applied")
    
is_day = True
if is_day == True:
    print("lights off!")

print("it is fun ")
score = 51
pass_grade = score > 50
if pass_grade:
    print("pass grade")
lost = score < 50
if lost:
    print("you are dumb")

print("this is realy fun")
song = "let me love you"
replay_time = 20
if replay_time > 15:
    print(f"you have played this song ({ song }) { replay_time} times")

diet = "hii"
veggie_resturent = "dharamshala"
nonveg_resturent = "naan vaala"
resturent = "dharamshala 2"
if  diet == "veg":
    print("try out: ")
    print(veggie_resturent) 
if  diet != "veg":
    print(f"nonveg m to {nonveg_resturent} milega bhaishab ")

print("this way can change the value further also")
age = 19
can_drive = False

if age > 18 :
    can_drive = True

print(can_drive) 



inbox_full = True
show_alart = inbox_full == True
if show_alart:
    print("beta inbox bher gaya")
    print("kuch delete ker deta , badi mherbani hoti")

    