# data frame a complete table with multiple rows
import pandas as pd

plant = {"Pressure": [520, 521, 518, 523, 519],
         "Temperature": [82.3, 82.5, 81.9, 82.7, 82.1],
         "Flow": [145, 146, 143, 147, 144],
         "Status": ["RUNNING", "RUNNING", "TRIP", "RUNNING", "RUNNING"]}

df = pd.DataFrame(plant)
#df.index.name = "Index"
#print(df["Pressure"])
#print(df[["Pressure", "Flow"]])
#print(df["Pressure"].mean())
#print(df["Pressure"].max())
#print(df["Pressure"].min())
print(df.loc[2])
print(df.loc[1:3, "Pressure"])