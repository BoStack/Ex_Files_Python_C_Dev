# Example file for the Python for the C# Developer LinkedIn Learning course by Joe Marini

# Exceptions in Python are similar to those in C#
# There's a try-except-finally mechansism

try:
    a = 30
    b= 0
    c=None

    #if(a>20):
    #   raise ValueError("Can't go higher than 20!")

    x= int(c)
        

    print("results is :", x)
except ZeroDivisionError as e:
    print("Whoopsiii!! the value is undifiend", e)
except ValueError as e:
    print("Iyhooo" , e)
except BaseException as e:
    print(e)
finally:
    print("running to infinity")