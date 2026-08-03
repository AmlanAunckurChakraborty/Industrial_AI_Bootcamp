#Basic For Loop
print("\nBASIC FOR LOOP\n")

count =1
i =1
for i in range(5): # range should be (last output + 1)
    print("number of iteration, outpiut : ",count,",",i) # i will start from 0 for this loop if i want to start i f4rom 1 then have to define the lower limit value of i as 1 also
    count +=1
   

# For Loop with defined range
print("\nFOR LOOP WITH DEFINED RANGE\n")

count =1
for i in range(5,11): # range should be (last output + 1)
    print("number of iteration, outpiut : ",count,",",i)
    count +=1


# For Loop with defined range and defined interval
print("\nFOR LOOP WITH DEFINED RANGE AND INTERVAL\n")

count =1
for i in range(6,31,3): # range should be (last output + 1)
    print("number of iteration, outpiut : ",count,",",i)
    count +=1


# Reverse For Loop with defined range and defined interval
print("\nREVERSE FOR LOOP\n")

count =1
for i in range(30,5,-3): # range should be (last output - 1)
    print("number of iteration, outpiut : ",count,",",i)
    count +=1


#Nested for loop
print("\nNested FOR LOOP\n")

for compressor in range(1, 4): # range should be (last output + 1)
    print("Compressor's Number:", compressor)
    for valve in range(1, 11): # range should be (last output + 1)
        print("Checking Valve's Number", valve)
    print()