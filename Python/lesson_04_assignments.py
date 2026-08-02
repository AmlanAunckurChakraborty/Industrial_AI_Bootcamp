# Lesson 04 - Assiginments (type,isinstance,id,input)

pressure = input("Enter the current pressure : ")      # kPa
temperature = float(68)      # °C
flow_rate = float(input("Enter flowrate : "))      # MMSCFD
run_status = True
unit_name = "A"

print("Compressor Outlet Pressure:", pressure, "kPa")
print("Gas Temperature:", temperature, "°C")
print("Gas Flow Rate:", flow_rate, "MMSCFD")
print("Run Status:", run_status)
print("Unit_name:",unit_name)

print()

print("pressure data type: ", type(pressure))
print("temperature data type: ", type(temperature))
print("flow rate data type: ", type(flow_rate))
print("run_status data type: ", type(run_status))
print("Unit Name data type: ", type(unit_name))

print()

print("pressure data type is int: ", isinstance(pressure,int))
print("temperature data type is float: ", isinstance(temperature,float))
print("flow rate data type is float: ", isinstance(flow_rate,float))
print("run_status data type is boolen: ", isinstance(run_status,bool))
print("Unit Name data type string: ", isinstance(unit_name,str))

"""
This lesson is short, but it's important to understand the idea behind it.

What is id()?

Every object in Python has:

a value
a type
an identity

The id() function returns the identity of an object.

Think of it like this:

Value = What's inside the box 📦
Type = What kind of box it is 📦
ID = The box's unique serial number 🏷️
"""
print()

print("pressure ID: ", id(pressure))
print("temperature ID: ", id(temperature))
print("flow rate ID: ", id(flow_rate))
print("run_status ID: ", id(run_status))
print("Unit Name ID: ", id(unit_name))