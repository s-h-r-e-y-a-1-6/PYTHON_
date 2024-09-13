def diff(n):
    if n > 17:
        return 2 * abs(n - 17)
    else:
        return 17 - n

n = int(input("Enter a number: "))
print("Difference from 17:", diff(n))
