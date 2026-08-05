#map (function, iterable) it perfor same function on each iterables
#normal funtion
print("====Normal functon using map ====")
def square(x):
    return x * x # pow(x, 2) it can also be used

numbers = [1,2,3,4]
result = list(map(square, numbers))
print(result)

# lambda with map
print("====Lambda using map ====")
numbers = [1,2,3,4]
result = list(map(lambda x: x ** 2, numbers))
print(result)

# converting sting to integer
numbers = input("Enter Numbers : ").split()
print(numbers)
numbers = list(map(int, input("Enter Numbers : ").split()))
print(numbers)

#real life example
pressure_bar = [30,32,35]
pressure_psi = list(map(lambda x: x * 14.5038,pressure_bar))
print(pressure_psi)

#filter
print("\n====== Filter =======\n")

numbers = [1,2,3,4,5,6,7,8,9,10]
result = list(filter(lambda x: x % 2 == 0, numbers))
print(result)

pressure = [520,525,530,540,550]
high_pressure = list(filter(lambda x: x > 530,pressure))
print(high_pressure)

compressors = [("A",True),("B",False),("C",True),("D",False)]
running = list(filter(lambda x: x[1],compressors))
print(running)

# zip
print("\n====ZIP====\n")

pressure = [520,530,540]
temperature = [42,43,44]
result = list(zip(pressure,temperature))
print(result)

# industrial example 
print("\n==Industrial Example==\n")
sensor = ["PT101","PT102","PT103"]
pressure = [520,530,540]
result = list(zip(sensor,pressure))
print(result) # its a dictionaries

#loop for zip
print("\n==Loop==\n")
for tag, value in zip(sensor,pressure):
    print(tag, value)