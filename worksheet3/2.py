def test_range(n):
    return 100 <= n <= 1000 or n == 2000

n = int(input("Enter a number: "))
print("Is the number within 100 to 1000 or 2000?\n", test_range(n))