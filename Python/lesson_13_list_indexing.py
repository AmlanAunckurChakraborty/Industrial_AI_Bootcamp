#basic indexing
print(".list indexing basic\n")
pressure = [500, 510, 520, 530]
# print(pressure[0],pressure[1],pressure[2],pressure[3],pressure[4]) simply give error after we have pressure[4] which the list doesnt have
print(pressure[0],pressure[1],pressure[2],pressure[3]) 
print(pressure[-1],pressure[-2],pressure[-3],pressure[-4]); #negetive position works differently reverse direction

#user defined indexing
print("\nuser defined indexing\n")
pressure = [None]
pressure = list(map(int,input("Enter pressure values: ").split()))
pressure[2]= 100
print(len(pressure))
print(pressure[0],pressure[2],pressure[5])

#for loop using len
print("\nuser defined indexing using len for loop\n")
pressure = list(map(int, input("Enter pressure values: ").split()))
for i in range(len(pressure)):
    print("Index:", i, "Value:", pressure[i])

#better practice
print("\nuser defined list in python syntex\n")
pressure = list(map(float, input("Enter pressure values: ").split()))
for value in pressure:
    print(value)

#with enumerate
print("\nuser defined list in python syntex with enumerate\n")
pressure = list(map(int, input("Enter pressure values: ").split()))
for index, value in enumerate(pressure):
    print("Index:", index, "Value:", value)
