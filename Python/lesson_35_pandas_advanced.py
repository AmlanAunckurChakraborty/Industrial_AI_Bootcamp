# data frame a complete table with multiple rows
import pandas as pd

plant = {"Pressure": [520, 521, 518, 523, 519],
         "Temperature": [82.3, 82.5, 81.9, 82.7, 82.1],
         "Flow": [145, 146, 143, 147, 144],
         "Status": ["RUNNING", "RUNNING", "TRIP", "RUNNING", "RUNNING"]}

df = pd.DataFrame(plant)
df.index.name = "Index"
"""
#loc
print(df["Pressure"])
print(df[["Pressure", "Flow"]])
print(df["Pressure"].mean())
print(df["Pressure"].max())
print(df["Pressure"].min())
print(df.loc[2])
print(df.loc[1:3, "Pressure"])
print(df.loc[1:3, ["Pressure", "Flow"]])

#iloc
print(df.iloc[2])
print(df.iloc[2, 0])
print(df.iloc[1:4])
print(df.iloc[1:4, 0:3])

#condition filtaring
print(df[df["Pressure"] > 520])
print(df[df["Pressure"] < 520])
print(df[df["Status"] == "TRIP"])
print(df[df["Status"] == "RUNNING"])
print(df[(df["Pressure"] > 520) & (df["Flow"] > 145)])
print(df[(df["Pressure"] > 520) | (df["Flow"] > 145)])
print(df[df["Status"] != "TRIP"])
print(df[df["Status"].isin(["TRIP", "RUNNING"])]) #only for multiple condition checking on single value here is status can perform with multiple like pressure a& flow
"""
#sorting
print("Assending low>high\n",(df.sort_values("Pressure")))
print("inplace\n",(df.sort_values("Pressure", inplace=True))) #not working
print("dessending high>low\n",(df.sort_values("Pressure", ascending=False)))
print("Multi condition sorting\n",(df.sort_values(["Status", "Pressure"], ascending=[True, False])))

#creating new column
df["Pressure_bar"] = df["Pressure"] / 100
print("new column\n",df)
df["Flow_per_Pressure"] = df["Flow"] / df["Pressure"]
print("multicolumn dependent new column\n",df)
df["High_Pressure"] = df["Pressure"] > 520
print("conditional new column\n",df)

#dropiing / deleting columns and rows
print("\n - hp\n")
print(df.drop(columns="High_Pressure"))
print("\n - p_bar and flow/pressure \n")
print(df.drop(columns=["Pressure_bar", "Flow_per_Pressure"]))
print("\n - index[1,3]\n")
print(df.drop(index=[1, 2, 3]))

#renaming
df = df.rename(columns={"Pressure": "Pressure_kPa"})
print("one column\n",df)
df = df.rename(columns={"Pressure": "Pressure_kPa",
                        "Temperature": "Temperature_C",
                        "Flow": "Flow_m3h"})
print("multi column\n",df)
df.index.name = "Record_ID"
print("index column\n",df)
print("Assending low>high\n",(df.sort_values("Record_ID"))) #need to use new name of the index record id other wise sort or any oftion or work

