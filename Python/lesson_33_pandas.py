import pandas as pd
print(pd.__version__)

#series one dimentional arrays for panda
pressure = pd.Series([520, 521, 518, 523, 519])
print("full pd",pressure)
print("data type",type(pressure))
print("length ",len(pressure))
print("max",pressure.max())
print("min",pressure.min())
print("mean",pressure.mean())
print("sum",pressure.sum())
print("standerd deviation",pressure.std())
print(pressure.describe())

# data frame a complete table with multiple rows
import pandas as pd

plant = {"Pressure": [520, 521, 518, 523, 519],
         "Temperature": [82.3, 82.5, 81.9, 82.7, 82.1],
         "Flow": [145, 146, 143, 147, 144],
         "Status": ["RUNNING", "RUNNING", "TRIP", "RUNNING", "RUNNING"]}

df = pd.DataFrame(plant)
#df.index.name = "Index"

print(df)
print(type(df))
print(df.shape)
print(df.columns)
print(df.dtypes)
print(df.info())
print(df.describe())
#df.to_csv("plant_data.csv")
#df.to_csv("plant", index=False)
df.index.name = "Index"
df.to_csv("plant.csv")
#df.to_csv("plant.csv", index=True, index_label="Index") # only assign index name during the exicution of the creation reading wont get it

df1 = pd.read_csv("plant.csv")
print("df1 printing",df1)