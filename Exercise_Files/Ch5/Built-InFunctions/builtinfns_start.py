# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# Define some data to use in our functions
numbers = [10, 6, 23, 15, 18, 59, 62, 7, 103, 29, 35]
names = ["Amy", "Adam", "Benjamin", "Elise", "Terry", "Ziggy"]
somestring = "The quick brown fox jumped over the lazy dog"

# TODO: The len function will return the length of any iterable
print(len(numbers))
print(len(somestring))

# TODO: min and max calculate the smallest and largest values
minimumNum = min(numbers)
maximumNum = max(numbers)
print("minimum numberis :" + str(minimumNum)  ,"maximum number is:" + str(maximumNum))

# TODO: min and max can also use a key function to provide a comparable value
minimumName = min(names , key=lambda y: len(y))
maximumName = max(names , key=lambda y: len(y))
print("minimum name is :" + minimumName  ,"maximum name is:" + maximumName)

# TODO: The sorted function will return a new sorted list from an iterable
print(sorted(numbers))
print(sorted(somestring))
print(sorted(names, key=lambda y: len(y) ))

# TODO: any and all can be used to perform a test on a set of data
print(any(len(a)>3 for a in names))
print(all(b>2 for b in numbers))