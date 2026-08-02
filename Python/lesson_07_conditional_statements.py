#Conditional Assignments

hh_pressure_setpoint = float(input("Enter HH Pressure Setpoint(PSIA):"))
h_pressure_setpoint = float(input("Enter H Pressure Setpoint(PSIA):"))
l_pressure_setpoint = float(input("Enter L Pressure Setpoint(PSIA):"))
ll_pressure_setpoint = float(input("Enter LL Pressure Setpoint(PSIA):"))
current_pressure = float(input("Enter Current Pressure(PSIG) :"))
 
if (current_pressure + 14.75) >= hh_pressure_setpoint:
    print("Pressure Is Critically High, Emergency Shutdown....!!!!!")
    A= "HH PRESSURE !!!"
elif (current_pressure + 14.75) >= h_pressure_setpoint and (current_pressure + 14.75) <= hh_pressure_setpoint:
    print("Pressure Is High, Take Imidiate Action....")
    A= "H PRESSURE ..."
elif (current_pressure + 14.75) <= l_pressure_setpoint and (current_pressure + 14.75) >= ll_pressure_setpoint:
    print("Pressure Is Low, Take Imidiate Action....")
    A= "L PRESSURE ..." 
elif (current_pressure + 14.75) <= ll_pressure_setpoint:
    print("Pressure Is Critically Low, Emergency Shutdown....!!!!!")
    A= "LL PRESSURE !!!"
else:
    print("Pressure Is In Normal Condition")
    A= "NORMAL PRESSURE" 
print (A)

#WOW THIS A IS PRINTED OUT OF THE ELES SO JUST HAVE TO MOVE THE NEXT COMMAND TO A SINGLE LINE TO DETACH FROM THE IF ELSE LOOP.PYTHON IS SIMPLE