# LESSON 19 - SET BASICS

print("\n========== SET ==========\n")

# User Defined Set
pressure = set(map(int, input("Enter Pressure Values: ").split()))
print("Set Length :", len(pressure),"Set Values",pressure)


# Duplicate Removal
print("\n========== DUPLICATE REMOVAL ==========\n")
pressure = {500, 510, 500, 520, 510, 530, 530}
print(pressure)

# Loop
print("\n========== LOOP ==========\n")
for value in pressure:
    print(value)

# Enumerate
print("\n========== ENUMERATE ==========\n")
for index, value in enumerate(pressure):
    print("Index:", index, "Value:", value)

# Membership Operators
print("\n========== MEMBERSHIP ==========\n")
print("500 in pressure :", 500 in pressure)
print("999 in pressure :", 999 in pressure)
print("700 not in pressure :", 700 not in pressure)

# No Indexing
print("\n========== INDEXING ==========\n")
# print(pressure[0]) ***** Sets do not support indexing. *****

# No Slicing
print("\n========== SLICING ==========\n")
# print(pressure[1:3]) ***** Sets do not support slicing. *****
print("")

# Why?
print("\n========== WHY? ==========\n")
pressure = {500, 510, 520, 530}
print("Set :", pressure)
print("\nOrder is not fixed.")
print("Therefore indexing and slicing are impossible.")
