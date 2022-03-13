from typing import ItemsView


class Person:
    def __init__(self,name,age):
        self.name =name
        self.age = age

    def sayhello(self):
        print("hello")

    def saybye(self):
        print("good bye")

teacher = Person("EMily ", 24)
teacher.sayhello()
teacher.saybye()

#////////////////////////////////[ can use all python build-in functions here]//////////////////////////////////////////////////////////////////////////////////////////
    

class Pie:
    def __init__(self,flavour,ingrediends):
        self.flavour = flavour
        self.ingrediends = ingrediends

    def print_ingrediends(self):
        for i in self.ingrediends :
            print(i)

apple_pie =Pie("apple",["flour","eggs","apples","butter"])

apple_pie.print_ingrediends() # show one by one ....
print(apple_pie.ingrediends)  # show as mentioned by us....

#///////////////////////////////////////////[  another example  ]/////////////////////////////////////////////////////////

class Book_series:
    def __init__(self,name , book):
        self.name = name
        self.book = book
        self.num_book = len(book)

    def print_name(self):
        print(self.name)

    def print_book(self):
        print(self.book)

hp = Book_series("pooter head",["hp1","hp2","hp3","hp4","hp5","hp6","hp7","hp8"])

print(hp.num_book)



#zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz





















