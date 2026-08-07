# data frame a complete table with multiple rows
import pandas as pd

plant = {"Pressure": [520, 521, 518, 523, 519],
         "Temperature": [82.3, 82.5, 81.9, 82.7, 82.1],
         "Flow": [145, 146, 143, 147, 144],
         "Status": ["RUNNING", "RUNNING", "TRIP", "RUNNING", "RUNNING"]}

df = pd.DataFrame(plant)
#df.index.name = "Index"

print("full table",df)
print("type",type(df))
print("shape",df.shape)
print("colunmns",df.columns)
print("dtypes",df.dtypes)
print("info",df.info())
print("describe",df.describe())
df.to_csv("plant_data.csv")
df.to_csv("plant", index=False)
df.index.name = "Index"
df.to_csv("plant.csv")
#df.to_csv("plant.csv", index=True, index_label="Index") # only assign index name during the exicution of the creation reading wont get it

df1 = pd.read_csv("plant.csv")
print("df1 printing",df1)