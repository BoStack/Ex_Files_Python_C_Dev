# Python for the C# Developer by Joe Marini
# Example code file for loops

# the Python for loop always acts as an iterator - the typical
# (init value, test, increment) pattern isn't something you see in Python

# TODO: to iterate over a count, you create a numerical iterator with range()
A= 5

for i in range(A):
    print(i, end= "")
print("\n---------")

for i in range (-5 ,5, 2):
    print(i, end= "")
print("\n---------")
FullName = "Beau Monese"
for B in FullName:
    print(B +"," ,end= "")
print("\n---------")

# TODO: if you really need an index, you can use enumerate()
for i ,B in enumerate(FullName):
    print(str(i)+ ","+ B + "," , end="")
print("\n---------")


# TODO: Similarly, there's only a while loop in python and no do-while, which
# is just syntactic sugar for a loop that always executes at least once
keepgoing = True
i = 1
x =123
pin= input("Enter your pin:")
while(keepgoing):
    print("num:" , i)
    i+=1
    if i <= 10:
        keepgoing =False


while({pin} != x and keepgoing):
   print("pin is correct ,Wellcome " ) if pin==123 else print("pincode incorrect please try again!! your attempt:"+ str(i))

   i+=1
   if i ==3 :
       print ("you account is blocked")
       keepgoing = False
            
