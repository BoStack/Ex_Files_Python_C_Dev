# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# functions are defined using the def keyword, then
# the : character and whitespace define the function body

def newfunc():
    print("This is the statemnt to my first fucntion")
    return 42

def newvoidfunc(a ,b):
    print("this fuction has no return value")
    print(a+b)

def var(a, b ,*args):
    print(a+b)
    for arg in args:
        print(arg)

val1 = newfunc()
print(val1)

val2= newvoidfunc(5, 5)
print(val2)

var( 10,15 , 'C', "Beau" ,5.555,)
