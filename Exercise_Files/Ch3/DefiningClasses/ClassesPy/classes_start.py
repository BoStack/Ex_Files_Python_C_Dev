# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Classes are defined using the class keyword
class Book:
    def __init__(self, title, author, price) :
        self._tittle = title
        self._author = author
        self._price = price

    @property
    def tittle(self):
        return self._tittle
    
    @tittle.setter
    def tittle(self,value) :
        self._tittle = value
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self,value1) :
        self._author = value1
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value2) :
        self._price = value2

# TODO: create an instance of the class
b1= Book("The monk who sold his ferari" ,"Robbin Shamar" ,100.00)
print("Title of the book is:" +b1._tittle)
print("The author of the book is:" +b1._author)
print("The price of the book is: R" +str(b1._price))
