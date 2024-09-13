L = [11, 12, 13, 14]

# (i) Add 50 and 60 to L
L.extend([50, 60])

# (ii) Remove 11 and 13 from L
L.remove(11)
L.remove(13)

# (iii) Sort L in ascending order
L.sort()

# (iv) Sort L in descending order
L.sort(reverse=True)

# (v) Search for 13 in L
if 13 in L:
    print("13 is in the list.")
else:
    print("13 is not in the list.")

# (vi) Count the number of elements present in L
print("Number of elements:", len(L))

# (vii) Sum all the elements in L
print("Sum of all elements:", sum(L))

# (viii) Sum all ODD numbers in L
print("Sum of all odd elements:", sum([x for x in L if x % 2 != 0]))

# (ix) Sum all EVEN numbers in L
print("Sum of all even elements:", sum([x for x in L if x % 2 == 0]))

# (x) Sum all PRIME numbers in L
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print("Sum of all prime elements:", sum([x for x in L if is_prime(x)]))

# (xi) Clear all the elements in L
L.clear()

# (xii) Delete L
del L
