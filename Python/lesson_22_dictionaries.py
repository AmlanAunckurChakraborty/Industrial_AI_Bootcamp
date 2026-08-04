# LESSON 20 - DICTIONARY
print("\n========== DICTIONARY ==========\n")

# CREATE
compressor = {"Pressure":520, "Temperature":42, "Flow":120, "Running":True}
compressor1 = {}
compressor2 = dict()
compressor1 = compressor.copy()
compressor2 = compressor.copy()
print("Original Dictionary")
print("compressor",compressor)
print("compressor1",compressor1)
print("compressor2",compressor2)

# LENGTH
print("\nDictionary Length")
print("dictionaries len:",(compressor))

# ACCESS VALUE
print("\nAccess Values")
print("prressure access",compressor["Pressure"])
print("temperature access",compressor["Temperature"])

# get()
print("\nget()")
print("prressure access with get()",compressor.get("Pressure"))
print("motor access with get()",compressor.get("Motor"))
print("motor no data with get()",compressor.get("Motor","Amlan, no Data bro!!!!")) #**** can define what to back also
print("motor no data with get()",compressor.get("Motor",int(120))) #**** the value can be any data type which we can use leter in program

# MODIFY VALUE
print("\nModify Value")
compressor["Pressure"] = 540
print("after modify pressure",compressor)

# ADD NEW KEY
print("\nAdd New Key")
compressor["Motor_Current"] = 34.5
print("after adding motor current",compressor)

# LOOP USING KEY
print("\nLoop Using Keys")
for key in compressor:
    print("print key with for loop",key)

# LOOP USING VALUES
print("\nLoop Using Values")
for value in compressor.values():
    print("print value with for loop",value)

# LOOP USING ITEMS
print("\nLoop Using Items")
for key, value in compressor.items():
    print("print item with for loop",key, ":", value)

# ENUMERATE
print("\nEnumerate")
for index, (key, value) in enumerate(compressor.items()):
    print("print enumerate , for loop",index, key, value)

# MEMBERSHIP
print("\nMembership")
print("print membership of pressure","Pressure" in compressor)
print("print membership of motor","Motor" in compressor)

# keys()
print("\nkeys()")
print("print",compressor.keys()) # ***** automatically print dict keys but will not mentaion the name od the keys we need to name them if more then one dictionaries

# values()
print("\nvalues()")
print(compressor.values())

# items()
print("\nitems()")
print(compressor.items())

# update()
print("\nupdate()")
compressor.update({"Pressure":560, "Temperature":45})
print(compressor)

# pop()
print("\npop()")
removed = compressor.pop("Flow")
print("Removed :", removed)
print(compressor)

# popitem()
print("\npopitem()")
removed = compressor.popitem()
print("Removed :", removed)
print(compressor)

# copy()
print("\ncopy()")
copy_compressor = compressor.copy()
print(copy_compressor)

# clear()
print("\nclear()")
copy_compressor.clear()
print(copy_compressor)

# NESTED DICTIONARY
print("\nNested Dictionary")
plant = {"Compressor_A":{"Pressure":520,"Temperature":42},"Compressor_B":{"Pressure":530,"Temperature":45},"Compressor_C":{"Pressure":120,"Temperature":41},"Compressor_D":{"Pressure":50,"Temperature":45}}
print("plant",plant)
print("plant compressor A",plant["Compressor_A"])
print("plant compressor A Pressure",plant["Compressor_A"]["Pressure"])
print("plant compressor c Temperature",plant["Compressor_C"]["Temperature"])

#update from nested
print("\n==========update()FROM ONE TO ANOTHER NESTED ALSO==========")
best_compressor_output = dict() # *** can use {} also
best_compressor_output.update({"pressure":plant["Compressor_A"]["Pressure"], "Temperature":plant["Compressor_C"]["Temperature"]})
print("BEST COMPRESSOR OUTPUTS",best_compressor_output)

plant = {"Compressor_A":{"Pressure":520,"Temperature":42},"Compressor_B":{"Pressure":530,"Temperature":45},"Compressor_B":{"Pressure":120,"Temperature":41},"Compressor_D":{"Pressure":50,"Temperature":45}}
print("same plant",plant)