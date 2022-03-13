# sometimes we want to raise an exception when a condition we have defined is not met
# we can create our own error line ....using [  raise  ]
# word after raise represents type of error [  Exception//ValueError//LookUpError]

#------------------------------[ Exception ]

slices =18
diners =0

if diners < 1:
    raise Exception("there should be one diner atleast")

else :
    slices_each = slices / diners

#--------------------------------[ ValueError ]

predicted_sales = -5
if predicted_sales < 0:
    raise ValueError("sales value can't be negative")


############################################[ SOMETHING DIFFERENT ]####################################################
#   try , except , pass and finally are use for exception handling
# work like : try kro ki [x and y add hojayein] agar na ho paye to error show kr do
# it is helpful , by getting error it doesn't terminate the code 
# we use pass if we don't want to write any code inexcept statement

age = 1000
try:
    adult_years = age - 18
except:
    raise TypeError("input is not a number")
else:
    if adult_years > 150:
        raise ValueError("age is too large")

##############################################[ example 2 ]###################################################################

# we can use a else statement at the end if we want to execute some code only when no error has been raised....

details = {
"name":"satyam",
"age":17,
"occupation":"student"
}

try:
    age = details["age"]
except:
    raise NameError("age value is not valid")
else:
    print(f"maximum heart rate is {220-age}")

##############################################[ example 3 ]###########################################################################
# we use finally for the code we want to run it doesn't matter above code gives error or not
entry = 50

try:
    result = entry * 1.5
except:
    raise ValueError("result can not be calculated")
else :
    print(result)
finally:
    print("wanna try another value???")



