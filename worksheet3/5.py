def distinct_elements(l):
    return list(set(l))

l = input("Enter a list of numbers separated by spaces: ").split()
l = [int(x) for x in l]
print("Distinct elements:", distinct_elements(l))

