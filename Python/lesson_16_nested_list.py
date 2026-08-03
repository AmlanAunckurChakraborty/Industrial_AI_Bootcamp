#nested list
print("\n========== NESTED LIST ==========\n")

compressor = []

rows = int(input("Enter Number of Compressors: "))
cols = int(input("Enter Number of Pressure Values per Compressor: "))

# Create Nested List
for i in range(rows):

    print("\nEnter Pressure Values for Compressor", i + 1)

    pressure = list(map(int, input().split()))

    compressor.append(pressure)

print("\nOriginal Nested List")
print(compressor)

# Access
print("\nAccess Element")
print(compressor[1][2])

# Modify
compressor[1][2] = 999

print("\nAfter Modification")
print(compressor)

# Append a New Row
compressor.append([100,200,300])

print("\nAppend New Row")
print(compressor)

# Append a Value
compressor[0].append(888)

print("\nAppend Value in First Row")
print(compressor)

# Extend a Row
compressor[0].extend([111,222])

print("\nExtend First Row")
print(compressor)

# Insert a New Row
compressor.insert(1,[55,66,77])

print("\nInsert New Row")
print(compressor)

# Insert a Value
compressor[0].insert(2,555)

print("\nInsert Value")
print(compressor)

# Remove a Value
compressor[0].remove(555)

print("\nRemove Value")
print(compressor)

# Pop a Value
removed_value = compressor[0].pop(1)

print("\nRemoved Value:", removed_value)
print(compressor)

# Copy
copy_compressor = compressor.copy()

print("\nCopied List")
print(copy_compressor)

# Nested Loop
print("\nNested Loop")

for row in compressor:
    for value in row:
        print(value, end=" ")
    print()

# Nested Loop with enumerate
print("\nNested Loop with Enumerate")

for row_index, row in enumerate(compressor):
    print("Row Number:", row_index)

    for column_index, value in enumerate(row):
        print("Column:", column_index, "Value:", value)




"""
print("\n========== NESTED LIST using f string ==========\n")

compressor = []

rows = int(input("Enter Number of Compressors: "))
cols = int(input("Enter Number of Pressure Values: "))

# Create Nested List
for i in range(rows):
    pressure = list(map(int, input(f"Enter Pressure of Compressor {i+1}: ").split()))
    compressor.append(pressure)

print("\nOriginal Nested List")
print(compressor)

# Access
print("\nAccessing Element")
print("Compressor 2 Pressure 3 :", compressor[1][2])

# Modify
compressor[1][2] = 999

print("\nAfter Modification")
print(compressor)

# Append Row
compressor.append([100,200,300])

print("\nAppend New Row")
print(compressor)

# Append Value
compressor[0].append(888)

print("\nAppend Value in First Row")
print(compressor)

# Extend Row
compressor[0].extend([111,222])

print("\nExtend First Row")
print(compressor)

# Insert Row
compressor.insert(1,[55,66,77])

print("\nInsert New Row")
print(compressor)

# Insert Value
compressor[0].insert(2,555)

print("\nInsert Value")
print(compressor)

# Remove Value
compressor[0].remove(555)

print("\nRemove Value")
print(compressor)

# Pop Value
removed = compressor[0].pop(1)

print("\nRemoved Value :",removed)
print(compressor)

# Copy
copy_compressor = compressor.copy()

print("\nCopied List")
print(copy_compressor)

# Loop
print("\nNested Loop")

for row in compressor:
    for value in row:
        print(value,end=" ")
    print()

# Enumerate
print("\nEnumerate")

for row_index,row in enumerate(compressor):
    for col_index,value in enumerate(row):
        print(row_index,col_index,value)
        
"""