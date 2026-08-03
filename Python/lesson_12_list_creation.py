#Basic list 
plant_data = [500,100.2]
print(plant_data)
print(type(plant_data))


#use split to scan multiple veriables value in one line (SPACE BETWEEN VALUES)
#IF OUTPUT USER GIVEES A B C ... N
pressure1, pressure2, pressure3 = input("Enter Pressure1 Pressure2 Pressure3: ").split() 
print(pressure1,"\n")
print(pressure2,"\n")
print(pressure3,"\n")

#IF OUTPUT USER GIVEES A,B,C,...,N (COMMA BETWEEN VALUE)
pressure1, pressure2, pressure3 = input("Enter Pressure1 Pressure2 Pressure3: ").split(",") 
print(pressure1,"\n")
print(pressure2,"\n")
print(pressure3,"\n")


#User defined list
pressure = input("enter pressure: ")
temp = input("enter temperature: ")
field_data = [pressure,temp]
print(field_data)

#single line
pressure1, pressure2, pressure3 = input("Enter Pressure1 Pressure2 Pressure3: ").split() 
print(pressure1,"\n")
print(pressure2,"\n")
print(pressure3,"\n")
temp1,temp2,temp3 = input("Enter Temperature1 Temperature2 Temperuture3: ").split()
print(temp1,"\n")
print(temp2,"\n")
print(temp3,"\n")
unit_data = [pressure1,temp1,pressure2,temp2,pressure3,temp3]
print(unit_data)

#using map to wrap everything in one line **** one drwaback only make list with one data type at a time, cant mix diff. datatype veriables****
pressure = list(map(int,input("Enter pressure1 pressure2 pressure3 values: ").split()))
temp = list(map(float,input("Enter temperature1 temperature2 temperature3 values: ").split()))
print(pressure)
print(temp)

# ***** for now we need to do this,but in function we will make funtions for this****
pressure, temperature, name = input().split()
pressure = int(pressure)
temperature = float(temperature)