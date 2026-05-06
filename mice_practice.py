import numpy as np
import pandas as pd
#load excel file
df = pd.read_excel(r"C:\Users\Administrator\Desktop\my_python\Data_Cortex_Nuclear.xls/Data_Cortex_Nuclear.xls")
print(df.head(10))
print(df.shape)
#show only control mice
control_mice = df[df["Genotype"] == "Control"]
print(control_mice.head(5))
#calculate mean and standard deviation
protein = np.array(df["DYRK1A_N"])
print("mean:" , np.mean(protein))
print("standard deviation:" ,np.std(protein))
