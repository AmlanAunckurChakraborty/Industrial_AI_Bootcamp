#write csv
with open("sensor.csv","w") as file:
    file.write("Time,Pressure,Temperature,Flow\n")
    file.write("08:00,520,82.3,145\n")
    file.write("08:01,521,82.4,146\n")

#appand csv
with open("sensor.csv","a") as file:
    file.write("08:02,519,82.2,144\n")

#read csv
with open("sensor.csv","r") as file:
    print(file.read())

import random as r
with open("sensor.csv","a+") as file:
    file.write("Pressure,Temperature,Flow\n")
    for _ in range(20):
        pressure = r.randint(500,550)
        temperature = round(r.uniform(75,90),2)
        flow = r.randint(130,160)
        file.write(f"{pressure},{temperature},{flow}\n")
        file.seek(0)
        print(file.read())