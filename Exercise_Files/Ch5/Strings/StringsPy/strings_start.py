# Example HelloWorld file for the Python for the C# Developer LinkedIn Learning course

thestr = "The quick brown fox jumps over the lazy dog"
alpha1 = "abcdef"
alpha2 = 'ABCDEF'

# TODO: getting the string length
print(len(thestr))

# TODO: working with substrings
print(thestr.startswith("The"))
print(thestr.endswith("dog"))
print(thestr.find("fox"))

print(thestr[4:9])

newstri =thestr.replace("fox" , "wolf")
print(newstri)

# TODO: string concatenation
stringlist = []
for x in range(10):
    stringlist.append(str(x))

thestr = "--".join(stringlist)
print(thestr)

# TODO: string interpolation
interpol = f"Lower case letters are {alpha1} ,uppercase are {alpha2}"
print(interpol)


