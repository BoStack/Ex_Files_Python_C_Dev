

keepgoing = True
total = 0
i= 0
print ("RunningTally(tm)")
print("Enter a number to the tally , enter 'quit' to stop")

while (keepgoing):
    num= input()
    if num == "quit":
        keepgoing = False
    else :
        
     i = int(num)
    total += i
    print(total)

     
