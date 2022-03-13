print("complex decision making")


age = 17 
has_permit = True
insuarence = True
if age >16 and has_permit and insuarence:
    print("can drive")
else:
    print(f"nikal { age} saal ki age m driving krega")

year = 1998
if year >1900 and year<2020 :
    print("valid entry")
else:
    print("invalid")

subway_defect = True
is_sunny = True
distance = 2
if subway_defect and is_sunny and distance <= 2 :
    print("kaam pe nikal")
else:
    print("kaam pe mt ja aaj")


print("we use or for alternative conditions , agar given conditions me se koi true ho jaye to bhi work kregi .")


average_grade =  "A"
final_score = 1100 
if average_grade == "A" or final_score >= 1300:
    print("certificate achieved")
else:
    print("na munna na tumhe na milega certificate")