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


