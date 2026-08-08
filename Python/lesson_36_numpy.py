import pandas as pd
import numpy as np

plant = {"Pressure": [520, 521, 518, 523, 519],
         "Temperature": [82.3, 82.5, 81.9, 82.7, 82.1],
         "Flow": [145, 146, 143, 147, 144],
         "Status": ["RUNNING", "RUNNING", "TRIP", "RUNNING", "RUNNING"]}

df = pd.DataFrame(plant)

df.loc[1, "Temperature"] = np.nan
print(df)
