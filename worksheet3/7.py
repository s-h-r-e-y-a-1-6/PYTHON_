def outer_function(x):
    def inner_function(y):
        return y + 10
    return inner_function(x)
   

x = int(input("Enter a number: "))
print("Result after processing:", outer_function(x))
