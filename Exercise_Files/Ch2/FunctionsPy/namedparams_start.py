# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# Functions can have default parameter values like in C#
# They can also be explicitly used in the calling location


# Functions can then be called using named parameters
# once you use a named parameter, all following params must be
# called by name as well

def assignedParams( x, y ,z ):
    if z:
        print("'x' comes first")
        print(x)
        print(y)
    else:
        print("'b' comes first")
        print(y)
        print(z)

assignedParams(5, y="hello" ,z= False)

