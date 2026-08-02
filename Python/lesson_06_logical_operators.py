#Logical Operators

suction_pressure = int(input("Enter current suction pressure:"))
discharge_pressure = float(input("Enter current discharge pressure:"))
final_pressure = int(input("Enter current final pressure:"))

print("\nSUCTION PRESSURE IS EQUAL TO DISCHARGE PRESSURE and SUCTINN PRESSURE IS NOT EQUAL TO Final PRESSURE:",suction_pressure == discharge_pressure and suction_pressure != final_pressure)
print("\nSUCTION PRESSURE IS GREATER THEN DISCHARGE PRESSURE and SUCTINN PRESSURE IS LESS THEN Final PRESSURE:",suction_pressure > discharge_pressure and suction_pressure < final_pressure)
print("\nSUCTION PRESSURE IS GREATER THEN DISCHARGE PRESSURE and SUCTINN PRESSURE IS LESS THEN Final PRESSURE:",suction_pressure > discharge_pressure or suction_pressure < final_pressure)
print("\nSUCTION PRESSURE IS LESS THEN EQUAL TO DISCHARGE PRESSURE and SUCTINN PRESSURE IS GREATER THEN EQUAL TO Final PRESSURE:",suction_pressure <= discharge_pressure and suction_pressure >= final_pressure)
print("\nSUCTION PRESSURE IS NOT LESS THEN EQUAL DISCHARGE PRESSURE:",not suction_pressure <= discharge_pressure)

# so we can also compare between integer and float in python