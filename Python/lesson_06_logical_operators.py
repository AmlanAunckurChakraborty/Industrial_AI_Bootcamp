#Logical Operators

suction_pressure = int(input("Enter current suction pressure:"))
discharge_pressure = float(input("Enter current discharge pressure:"))
final_pressure = 67

print("\nSUCTION PRESSURE IS EQuAL TO DISCHARGE PRESSURE:",suction_pressure == discharge_pressure)
print("\nSUCTINN PRESSURE IS NOT EQuAL TO DISCHARGE PRESSURE:",suction_pressure != discharge_pressure)
print("\nSUCTION PRESSURE IS GREATER THEN DISCHARGE PRESSURE:",suction_pressure > discharge_pressure)
print("\nSUCTION PRESSURE IS LESS THEN DISCHARGE PRESSURE:",suction_pressure < discharge_pressure)
print("\nSUCTION PRESSURE IS GREATER THEN EQUAL TO DISCHARGE PRESSURE:",suction_pressure >= discharge_pressure)
print("\nSUCTION PRESSURE IS LESS THEN EQUAL DISCHARGE PRESSURE:",suction_pressure <= discharge_pressure)

# so we can also compare between integer and float in python