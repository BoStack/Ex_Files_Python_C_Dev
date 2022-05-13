# Example file for the Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Variables can be declared without an explicit type


from ast import Global


lang = 'python'
print (lang)
lesson = 1
print (lesson)
Q = True
print (Q)

print(Q ,lang)


# TODO: re-declaring the variable works
Q = False
print(Q)

# TODO: ERROR: variables of different types cannot be combined

mixedVar = "YOu Number:"
print(mixedVar + str(1))

# TODO: Global vs. local variables in functions

def whatever():
    
    Q = "Papao"
    print(Q)

whatever()
print(Q)

# TODO: use the del operator to un-declare a variable
