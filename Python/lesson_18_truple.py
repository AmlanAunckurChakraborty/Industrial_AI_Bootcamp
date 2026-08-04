#tuple can not change after creation so list changing or shoting methods wont work also we can say its immutable
print("\ntuple\n")

pressure = tuple(map(int, input("Enter pressure values: ").split()))
print("tuple lenght:",len(pressure),"\n","tuple value :",pressure)
print("tuple count: ",pressure.count(4))
print("tuple index: ",pressure.index(4))
#enumerate can be done
for index, value in enumerate(pressure):
    print(index, value)
# slicing can be done as its not changing the the tuple but just pulling the values we want
print("\nSLICING\n")
# CAN NOT CHANGE THE TUPLE BUT CAN CHANGE IN VERIABLE SO WE CAN REDEFINE SAME VERIABLE TO SAME NEW TUPLE 
# Tuple cannot be modified.
# The variable can point to a new tuple.
pressure = (500,510,520,530,540) 
print(pressure[1:4])
print(pressure[::2])
print(pressure[::-1])

#PACKING
print("\nPACKING\n")
compressor = ("A", 520, 38.5, True)
print(compressor)

#UNPACKING
print("\nUNPACKING\n")
pressure = (500,510,520)
P1, P2, P3 = pressure
print(P1)
print(P2)
print(P3)
# list methods dont work for tuple
# pressure.append(30)
# print("list append: ",pressure) ***** tuple cant changed after creation so append cant work
# pressure.append([30,45])
# print("list append: ",pressure) ***** if i append ([3,4]) it will take it as a whole [3,4] and add as a member single one, and then we cant run the code as no ther element is list like this one
# pressure.extend([30,45])         ***** tuple cant changed after creation so extend cant work
# print("list extend: ",pressure)
# pressure.remove(30)              ***** tuple cant changed after creation so remove cant work
# print("list remove: ",pressure)
# pressure.insert(3,45)             ***** tuple cant changed after creation so insert cant work
# print("list insert: ",pressure)   
# removed_value = pressure.pop(3)   ***** tuple cant changed after creation so remove cant work
# print("removed value:", removed_value)
# print("list pop: ",pressure)      ***** tuple cant changed after creation so pop cant work
# copy_pressure = pressure.copy()   ***** tuple has no copy() method because it is immutable
# print("list copy: ",copy_pressure)
# copy_pressure.clear()               ***** tuple cant changed after creation so clear cant work
# print("list clear: ",copy_pressure)
# pressure.sort()                     ***** tuple cant changed after creation so extend cant work
# print("list sort: ",pressure)
# pressure.reverse()                  ***** tuple cant changed after creation so extend cant work
# print("list reverse: ",pressure)
# pressure.sort()
# print("list sort: ",pressure)
