def even_numbers(lst):
    return [num for num in lst if num % 2 == 0]

lst = input("Enter a list of numbers separated by spaces: ").split()
lst = [int(x) for x in lst]
print("Even numbers:", even_numbers(lst))
