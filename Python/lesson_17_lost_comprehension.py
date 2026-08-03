#list comprehension

# List Comprehension

print("\n========== LIST COMPREHENSION ==========\n")

pressure = list(map(int, input("Enter Pressure Values: ").split()))

print("\nOriginal List")
print(pressure)

# Copy List
copy_pressure = [value for value in pressure]

print("\nCopy List")
print(copy_pressure)

# Multiply Every Value by 2
double_pressure = [value * 2 for value in pressure]

print("\nMultiply by 2")
print(double_pressure)

# Convert kPa to Bar
pressure_bar = [value / 100 for value in pressure]

print("\nkPa to Bar")
print(pressure_bar)

# Square Every Value
square_pressure = [value * value for value in pressure]

print("\nSquare Values")
print(square_pressure)

# Select Even Values
even_pressure = [value for value in pressure if value % 2 == 0]

print("\nEven Values")
print(even_pressure)

# Select Odd Values
odd_pressure = [value for value in pressure if value % 2 != 0]

print("\nOdd Values")
print(odd_pressure)

# Values Greater Than 500
high_pressure = [value for value in pressure if value > 500]

print("\nPressure Greater Than 500")
print(high_pressure)

# Values Less Than 500
low_pressure = [value for value in pressure if value < 500]

print("\nPressure Less Than 500")
print(low_pressure)

"""
print("\n========== LIST COMPREHENSION CHATGPT==========\n")

pressure = list(map(int,input("Enter Pressure Values: ").split()))
print("\nOriginal")
print(pressure)

# Basic Copy
A = [i for i in pressure]
print("\nCopy")
print(A)

# Multiply
B = [i*2 for i in pressure]
print("\nMultiply by 2")
print(B)

# Divide
C = [i/100 for i in pressure]
print("\nkPa to Bar")
print(C)

# Square
D = [i*i for i in pressure]
print("\nSquare")
print(D)

# Even
E = [i for i in pressure if i%2==0]
print("\nEven")
print(E)

# Odd
F = [i for i in pressure if i%2!=0]
print("\nOdd")
print(F)

# Greater than 500
G = [i for i in pressure if i>500]
print("\nGreater than 500")
print(G)

# Less than 500
H = [i for i in pressure if i<500]
print("\nLess than 500")
print(H)

# String Conversion
I = [str(i) for i in pressure]
print("\nConvert to String")
print(I)

# Boolean
J = [i>500 for i in pressure]
print("\nBoolean")
print(J)

"""