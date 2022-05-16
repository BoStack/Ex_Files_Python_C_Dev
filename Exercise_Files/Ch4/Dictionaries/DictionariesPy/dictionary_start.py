# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# declare an empty dictionary
fileDesc = {}
# dictionaries can also be declared with initial content
nums = {1: "one", 2: "two", 3: "three"}

# TODO: add some items
fileDesc["pdf"] = "Portable Documents format"
fileDesc["txt"]="text file"
fileDesc["rtf"]="rich text form"
fileDesc["jpg"]="jpeg image"
fileDesc["png"]="portable network graphic image"
 

# TODO: get the item count
print(f"Dictionary contians {len(fileDesc)} items")

# TODO: adding an existing key just replaces the item
fileDesc["png"]= "Png"
print(fileDesc["png"])

# TODO: check if a key exists
print("txt" in fileDesc.keys())

# TODO: check if a value exists
print("jpeg image" in fileDesc.values())

# TODO: remove a single item
del fileDesc["pdf"]
print(f"Dictionary contians {len(fileDesc)} items")

# TODO: clear all values
fileDesc.clear()
print(f"Dictionary contians {len(fileDesc)} items")
