# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# define a list of days in English and French
days = ["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"]
daysFr = ["Dim", "Lun", "Mar", "Mer", "Jeu", "Ven", "Sam"]
daysdict = {"Sun": "Dim", "Mon": "Lun", "Tue": "Mar",
            "Wed": "Mer", "Thu": "Jeu", "Fri": "Ven", "Sat": "Sam"}

# TODO: iterate over a list
print("using iter:")
x = iter(days)
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x))
print(next(x)) 

#ALl the below section its not clear to me , i still need to fully understand it.
# TODO: iterate over a dictionary
print("dictionary iteration:")
for key in daysdict:
    print(key, ":" , daysdict[key])

print("\n---------\n")

for k ,v in daysdict.items():
    print(k, ":" ,v)

# TODO: use the enumerate function
print("using enumerate:")
for x,m in enumerate (daysFr, start=1):
    print(x, m)


# TODO: use the zip function
print("using zip:")
for m in zip(days,daysdict):
    print(m)

# TODO: combine enumerate and zip
print("using enumerate with zip:")

for i,m in enumerate(zip(days, daysFr,), start=1):
    print(f"Day {i} ,{m[0]} is {m[1]} in Italian")
