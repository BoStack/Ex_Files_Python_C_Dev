# Python for the C# Developer by Joe Marini
# Example code file for conditional statements

# Python only has an if/elif/else construct, unlike C#
# which supports switch statements

x = 150
y = 25
z = 10
G = 1
H = 125

A = "Result1"
B = "Result2"
C = "Result3"
# TODO: define an if-elif-else structure
num1 =int(input("enter first number"))

num2= int(input("enter first number"))


if x < y :
    print(A)
    print("--------------")
elif z > y and   y<z :
    print(B)
    print("--------------")
elif G == x or  G== 1 :
    print("Play with it")
    print(num1 + num2)
elif H != 5:
    print("The condition is true")
    print("--------------")
else:
    print(C)

# TODO: use the compact if-else format

print("You moving chief") if x <y else print (z + y)
