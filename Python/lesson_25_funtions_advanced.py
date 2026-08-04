#args srore as a truple
print("\n========== **args ==========\n")
def compressor(name, *pressure): # *args helps to take multiple veriables instead of fixing one position
    print(name)
    print(pressure)

print(compressor("Cmp A", 500))
print(compressor("Cmp A", 500,510,520,530))

#kwargs store as dictionaries
print("\n========== **kwargs ==========\n")
def compressor(name, **sensor): #by one star (*a) we make args and by two star (**a) we make kwargs with a normal variable name
    print("\nCompressor :", name)
    print("\nSensors")
    for key, value in sensor.items():
        print(key, ":", value)
compressor("Compressor_A",Pressure=520,Temperature=42,Flow=120)
compressor("Compressor_B",Pressure=540,Temperature=45,Flow=130,Current=34.5,Running=True)

#lambda write  a single executable function in one line
print("\n========== LAMBDA ==========\n")
# Addition (aritmatic)
add = lambda a, b: a + b
print("Addition :", add(10,20))

# Square
square = lambda x: x * x
print("Square :", square(5))

# Pressure Difference
pressure_difference = lambda suction, discharge: discharge - suction
print("Pressure Difference :", pressure_difference(20,45))

# Compressor Efficiency
efficiency = lambda output, input: (output / input) * 100
print("Efficiency :", efficiency(95,100))

# Highest Pressure
highest = lambda a, b: a if a > b else b
print("Highest Pressure :", highest(540,520))

#iinother functions
numbers = [1,2,3,4]
result = map(lambda x: x * 2, numbers)
for value in result:
    print(value)

result = list(map(lambda x: x * 2, numbers))
print("\nresult with list map and lembda\n",result)

result = tuple(map(lambda x: x * 2, numbers))
print("\nresult with touple map and lembda\n",result)

result = set(map(lambda x: x * 2, numbers))
print("\nresult with set map and lembda\n",result)

# better understanding lembda
result = map(lambda x: x * 2, numbers)

for value in result:
    print(value)

print(list(result)) # **** result now print a list but with out any value as map is an iterator