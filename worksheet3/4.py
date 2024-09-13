def count_upper_lower(s):
    upper_count = sum(1 for c in s if c.isupper())
    lower_count = sum(1 for c in s if c.islower())
    return upper_count, lower_count

s = input("Enter a string: ")
upper_count, lower_count = count_upper_lower(s)
print("Upper case letters:", upper_count)
print("Lower case letters:", lower_count)
