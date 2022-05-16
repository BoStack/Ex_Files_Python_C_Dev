# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

qrspace = []
newlist = [1, False, "bob"]

# TODO: append data to a list
qrspace.append("james")
qrspace.extend(["nathan" ,"allucious" , "takalani","andrew"])
print(qrspace)

# TODO: insert data
qrspace.insert(4,"mboni")
print(qrspace)

# TODO: search for a list item
print("Sibusiso" in qrspace)
print("james" in qrspace)
print(qrspace.index("nathan"))

# TODO: modify an item in-place
qrspace[3] = "Beau"
print(qrspace)
# TODO: remove an item
qrspace.remove("Beau")
print(qrspace)

# TODO: empty the list
qrspace.clear()
print(qrspace)

# TODO: lists can be created using the list() global function
surname = list("Monese")
print(surname)

num = list(range(1,10,3))
print(num)