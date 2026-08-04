# Functons 
def compressor():

    print("Compressor Running")

compressor()

def compressor_status(name, pressure):

    print(name)

    print("Pressure :", pressure)

    print()

compressor_status("Compressor A",520)

compressor_status("Compressor B",545)

compressor_status("Compressor C",510)

#return
def pressure():
    #print(name,"pressure")
    print("amlan") 
    return 520 
p = pressure() #print bothout put and return
print(p)
pressure() # print oonly the name or funtion output amlan 

#another example
def unit(A,B):
      print("Substraction") #if it print or do any action dont use return ,or exicute mukltiple calculation then also donnt use return,dont need return 0
      return A-B # If the function is supposed to calculate something, return the calculated value.
s = unit(10,5)
print(s)
unit(20,10) #### dont execute the return thing so also need to have a new veriable to define funtion first
#### The function still executes.
#### The returned value is ignored because it is not stored or used
if unit(10,5) > 2:
    print(unit(30,19)) ### unit() has the return also so have to print or use it compleately
    print("Alarm")

#scope (global& local veriables)
plant_status = "Running" # global
def emergency_shutdown():
    plant_status = "Trip" #local
    print(plant_status) #inside the function so print local
       
emergency_shutdown()

print(plant_status) #outside the function so print global
# same one using keyword global
plant_status = "Running"

def emergency_shutdown():
    global plant_status # by using global key word we make the change global change now both will be modified local and global
    plant_status = "Trip"

emergency_shutdown()

print(plant_status)

# argumets (default & keyword)
print("\n========= Default Arguments ===========")
def unit(parameter1_name,value1,unit_name = "Compressor - A",parameter2_name="temperature",value2 = float(83.2)):
    print(unit_name)
    print(parameter1_name)
    print(value1)
    print(parameter2_name)
    print(value2)
   
print("\ndefault with normal: ",unit("pressure",20))
print("\noverride default: ",unit("pressure",20,"Compressor - B","temperature",75.2)) # WE HAVE TO CHANGE TEMPERATURE ALSO AS WE CANT CHANGE 1 AND 3 FIX DEAFULT ARGUMETS ONLY 
print("\noverride default: ",unit("pressure",20,"Compressor - B")) # WE can change from the first to any number we want up to last but need to do for all till where we want
# ********** This issue will be fixed with keyword argumets ********
print("\nonly default parameters",unit("pressure",20,"Compressor - B", value2 = 75.2)) # It still works because Python matches by parameter name, not by position.

#### as no reture is defined in the function and we are printing them directly so as we discussed earlier it has no return so printing none.