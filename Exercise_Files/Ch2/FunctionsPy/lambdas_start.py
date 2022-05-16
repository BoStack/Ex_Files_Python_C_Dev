# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

data = [10, 6, 23, 15, 18, 59, 62, 7, 103, 29, 35]
name = ["beau", "tK", "alluta", "Yakshin", "elton", "james"]
# regular sort
print("Sorted:")
result = sorted(data)
print(result)

# TODO: sort using a lambda
print("Sort by first digit:")

reslt = sorted (data, key= lambda x:str(x) [0])
print(reslt)

reslt = sorted(name)
print(reslt)

reslt = sorted (name, key= lambda x:str(x) [1])
print(reslt)