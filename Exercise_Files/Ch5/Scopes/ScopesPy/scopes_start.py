# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Python uses the "with" statement to define a scope block
with open("MyTextFile.txt","r") as Bofile:
    linecount = 0
    while True:
        tstring = Bofile.readline()
        if not tstring:
            break
        print(tstring)
        linecount +=1

    print(f"The file has this {linecount} many lines" )
