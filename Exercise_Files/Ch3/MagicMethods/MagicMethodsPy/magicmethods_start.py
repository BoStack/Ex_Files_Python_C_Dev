# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini


class magicmethods():
    def __init__(self, name, size):
        self._name = name
        self._size = size

    def __str__(self):
        return f"My methods objects are {self._name} is {self._size}"
    
    def __repr__(self):
        return f"<magic mehtod class (name:{self._name}),(size.{self._size})"
    
    def __eq__(self,other):
        return self._name == other._name and self._size == other._size



mm1 = magicmethods("Obj1", 10)
mm2 = magicmethods("Obj2", 20)
mm3 = magicmethods("Obj1", 10)

print(mm1)
print(mm2)
print(mm3)

print(repr(mm1))
print(repr(mm2))

print(mm1== mm2)
print(mm1 == mm3)

