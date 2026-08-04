# LESSON 19.2 - SET METHODS

print("\n========== SET METHODS ==========\n")
pressure = set(map(int, input("Enter Pressure Values: ").split()))
print("Original Set :", pressure)

# add()
pressure.add(100)
print("\nadd() :", pressure)

# update()
pressure.update([200,300,400])
print("update() :", pressure)

# remove()
pressure.remove(100)
print("remove() :", pressure)

# discard()
pressure.discard(999)
print("discard() :", pressure)

# pop()
removed_value = pressure.pop()
print("Removed Value :", removed_value)
print("pop() :", pressure)

# copy()
copy_pressure = pressure.copy()
print("copy() :", copy_pressure)

# clear()
copy_pressure.clear()
print("clear() :", copy_pressure)