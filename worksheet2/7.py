import random
import string

def random_string(length):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for _ in range(length))

for _ in range(100):
    print(random_string(random.randint(6, 8)))



def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = [n for n in range(600, 801) if is_prime(n)]
print(primes)




divisible_by_7_and_9 = [n for n in range(100, 1001) if n % 7 == 0 and n % 9 == 0]
print(divisible_by_7_and_9)
