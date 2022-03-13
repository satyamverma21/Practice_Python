#sometimes we will need to update data inside a string without creating a whole new string .
# like updating a daily lunch special
special = "today's special is pasta "
new_special = special.replace("pasta" , "pizza")# pasta convert to pizza
print(new_special)

# instead of creating a new variable we can  reassign the original value
day = "today is sunday"
day  = day.replace("sunday" , "monday")
print(day)