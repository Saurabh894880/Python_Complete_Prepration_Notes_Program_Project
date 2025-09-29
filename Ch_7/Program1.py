#WAP To check the given number is prime or not
num = int(input("Enter a number: "))
is_prime = True
if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
if is_prime:
    print(num, "is a prime number.")
else:
    print(num, "is not a prime number.")

# second code for checking for prime number

num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")

# third code for checking for prime number using an list in O(n) time complexity 
num1 = int(input("Enter a number: "))
if num1 > 1:
    primes = []
    for num in range(2, num1 + 1):
        is_prime = True
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    print("Prime numbers up to", num1, "are:", primes)