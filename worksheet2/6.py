S1 = {10, 20, 30, 40, 50, 60}
S2 = {40, 50, 60, 70, 80, 90}

# (i) Add 55 and 66 in Set S1
S1.update([55, 66])

# (ii) Remove 10 and 30 from Set S1
S1.difference_update([10, 30])

# (iii) Check whether 40 is present in S1
print("40 is in S1") if 40 in S1 else print("40 is not in S1")

# (iv) Find the union between S1 and S2
print("Union of S1 and S2:", S1.union(S2))

# (v) Find the intersection between S1 and S2
print("Intersection of S1 and S2:", S1.intersection(S2))

# (vi) Find the S1 - S2
print("Difference between S1 and S2:", S1.difference(S2))
