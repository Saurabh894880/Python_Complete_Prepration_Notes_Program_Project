# Operators in Python
# 1. Arithmetic Operators
a = 10
b = 5
c = a + b # Addition
d = a - b  # Subtraction
e = a * b # Multiplication
f = a / b # Division
g = a % b # Modulus
h = a ** b # Exponentiation
i = a // b # Floor Division
print("Arithmetic Operators:")
print("Addition:", c)
print("Subtraction:", d)
print("Multiplication:", e)
print("Division:", f)
print("Modulus:", g)
print("Exponentiation:", h)
print("Floor Division:", i)

# 2. Comparison Operators
x = 10
y = 5
print("\nComparison Operators:")
print("Equal to:", x == y)
print("Not equal to:", x != y)
print("Greater than:", x > y)
print("Less than:", x < y)
print("Greater than or equal to:", x >= y)
print("Less than or equal to:", x <= y)
# 3. Logical Operators
p = True
q = False
print("\nLogical Operators:")
print("Logical AND:", p and q)
print("Logical OR:", p or q)
print("Logical NOT:", not p)
# 4. Assignment Operators
m = 10
n = 5
print("\nAssignment Operators:")
m += n # m = m + n
print("m += n:", m) 
m -= n # m = m - n
print("m -= n:", m)
m *= n # m = m * n
print("m *= n:", m)
m /= n # m = m / n
print("m /= n:", m)
m %= n # m = m % n
print("m %= n:", m)
m **= n # m = m ** n
print("m **= n:", m)
m //= n # m = m // n
print("m //= n:", m)

# 5. Bitwise Operators
a = 10 # In binary: 1010
b = 4  # In binary: 0100
print("\nBitwise Operators:")

print("Bitwise AND:", a & b) # 0000
print("Bitwise OR:", a | b)  # 1110 
print("Bitwise NOT:", ~a)    # 0101
print("Bitwise XOR:", a ^ b) # 1110
print("Left Shift:", a << 1) # 10100
print("Right Shift:", a >> 1) # 0101

# 6. Membership Operators
list1 = [1, 2, 3, 4, 5]
print("\nMembership Operators:")
print("Is 3 in list1?", 3 in list1)
print("Is 6 not in list1?", 6 not in list1)

# 7. Identity Operators
x = 10
y = 10
z = 5
print("\nIdentity Operators:")

print("Is x identical to y?", x is y)
print("Is x not identical to z?", x is not z)   
print("ID of x:", id(x))
print("ID of y:", id(y))

print("ID of z:", id(z))

a = [1, 2, 3]
b = a
print("Is a identical to b?", a is b)
print("ID of a:", id(a))
print("ID of b:", id(b))    