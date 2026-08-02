# Lesson 02 - Variables & Datatype

pressure = 950        # kPa
temperature = float(68)      # °C
flow_rate = 45.7      # MMSCFD
run_status = True
unit_name = "A"

print("Compressor Outlet Pressure:", pressure, "kPa")
print("Gas Temperature:", temperature, "°C")
print("Gas Flow Rate:", flow_rate, "MMSCFD")
print("Run Status:", run_status)
print("Unit_name:",unit_name)

print()

print("pressure data type: ", type(pressure))
print("temperature data type: ", type(temperature))
print("flow rate data type: ", type(flow_rate))
print("run_status data type: ", type(run_status))
print("Unit Name data type: ", type(unit_name))