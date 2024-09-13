D = {1: 5.6, 2: 7.8, 3: 6.6, 4: 8.7, 5: 7.7}

# (i) Add new entry in D; key=8 and value is 8.8
D[8] = 8.8

# (ii) Remove key=2
D.pop(2)

# (iii) Check whether key 6 is present in D
print("6 is present in D") if 6 in D else print("6 is not present in D")

# (iv) Count the number of elements present in D
print("Number of elements in D:", len(D))

# (v) Add all the values present in D
print("Sum of all values in D:", sum(D.values()))

# (vi) Update the value of 3 to 7.1
D[3] = 7.1

# (vii) Clear the dictionary
D.clear()
