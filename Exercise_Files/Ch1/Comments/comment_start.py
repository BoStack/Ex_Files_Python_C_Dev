# Python for the C# Developer LinkedIn Learning course by Joe Marini
# Example file for creating comments
'''this is a module level string
it can be put inside funcions and module levels
'''


def main():
    '''this is how to create a docstring string 
    a docstring is string with multiple lines 
    It is also compliled in the code while running
    in order to access it you use the __doc__
    '''
    # TODO: create a docstring that can contain multi-line information
    print(main.__doc__)

    # TODO: In python, comments are created using hash characters.
    print("Hello World")


if __name__ == "__main__":
    main()
