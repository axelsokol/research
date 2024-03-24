import numpy as np
import pandas as pd

df = pd.read_csv("C:\\Users\\osokolov\\Desktop\\Python Mix\\cerial_data\\cerial_data\\cereal.csv" )

print(df.describe())
print(df.head(10 ))
print(df[["Cereal Name","Calories"]])
print(df[5:12][1:5])
#df.iloc [row index range, column index range]
print(df.iloc[1:5, 0:5])
print("\n---- df.loc\n", df.loc[[1, 2, 3, 10, 12],['Cereal Name', 'Manufacturer']])

# https://www.youngwonks.com/blog/top-10-ways-to-filter-pandas-dataframe

'''
some modifications were performed after fork the original
'''

