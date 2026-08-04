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