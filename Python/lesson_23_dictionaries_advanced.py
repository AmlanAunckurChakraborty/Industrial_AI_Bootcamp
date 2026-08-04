print("\n========== REMAINING DICTIONARY TOPICS ==========\n")

# -------------------------------------------------
# DICTIONARY COMPREHENSION
# -------------------------------------------------

print("\n========== DICTIONARY COMPREHENSION ==========\n")

square = {x: x*x for x in range(1,6)}

print("Square Dictionary")
print(square)

cube = {x: x*x*x for x in range(1,6)}

print("Cube Dictionary")
print(cube)


# -------------------------------------------------
# DYNAMIC DICTIONARY
# -------------------------------------------------

print("\n========== DYNAMIC DICTIONARY ==========\n")

compressor = {}

compressor["Pressure"] = int(input("Enter Pressure : "))
compressor["Temperature"] = int(input("Enter Temperature : "))
compressor["Flow"] = int(input("Enter Flow : "))
compressor["Running"] = input("Running(True/False): ")

print(compressor)


# -------------------------------------------------
# DICTIONARY INSIDE LIST
# -------------------------------------------------

print("\n========== DICTIONARY INSIDE LIST ==========\n")

compressors = [

    {"Name":"A","Pressure":520,"Temperature":42},

    {"Name":"B","Pressure":530,"Temperature":44},

    {"Name":"C","Pressure":510,"Temperature":40}

]

print(compressors)

print("\nPrint all compressors\n")

for compressor in compressors:
    print(compressor)

print("\nOnly Pressure\n")

for compressor in compressors:
    print(compressor["Pressure"])

print("\nName and Temperature\n")

for compressor in compressors:
    print(compressor["Name"], compressor["Temperature"])


# -------------------------------------------------
# LIST INSIDE DICTIONARY
# -------------------------------------------------

print("\n========== LIST INSIDE DICTIONARY ==========\n")

plant = {

    "Pressure":[520,530,540],

    "Temperature":[42,44,46],

    "Flow":[120,125,130]

}

print(plant)

print("\nPressure List")

print(plant["Pressure"])

print("\nSecond Pressure")

print(plant["Pressure"][1])

print("\nLoop Pressure")

for pressure in plant["Pressure"]:
    print(pressure)


# -------------------------------------------------
# MIXED EXAMPLE
# -------------------------------------------------

print("\n========== MIXED EXAMPLE ==========\n")

plant = {

    "Compressor_A":{

        "Pressure":[520,521,522],

        "Temperature":[42,43,44]

    },

    "Compressor_B":{

        "Pressure":[530,531,532],

        "Temperature":[45,46,47]

    }

}

print(plant)

print("\nCompressor A Pressure List")

print(plant["Compressor_A"]["Pressure"])

print("\nSecond Pressure of Compressor B")

print(plant["Compressor_B"]["Pressure"][1])

print("\nLoop Compressor A Pressure")

for pressure in plant["Compressor_A"]["Pressure"]:
    print(pressure)