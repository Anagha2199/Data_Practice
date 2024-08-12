import pandas as pd
import numpy as np

df = pd.read_csv("income.csv")
print(df)
print("\n")
income_dc = df.columns
print("Columns of the file : ",income_dc)
print("\n")
print("First 2 column names : ",income_dc[:2])
print("\n")
print("Data types of all columns in csv : ",df.dtypes)
print("\n")
df.Y2008 = df.Y2008.astype(float)
print("Changed the datatype for column Y2008 : ",df.dtypes)
print("No of rows and columns : ",df.shape)
print("No of rows : ",df.shape[0])
print("No of columns : ",df.shape[1])
print("First 5 rows of csv by default : ",df.head())
print("Last 5 rows of csv by default : ",df.tail())
print("First 18 rows of csv : ",df.head(18))
print("Last 23 rows of csv : ",df.tail(23))
print("First 7 records of csv",df.iloc[0:7])
print("First 7 records of csv",df[0:7])
print(df.count())

print("Distinct Values of column index : ")
u_values = df.index.unique()
print(u_values,len(u_values))

print(pd.crosstab(df.Index,df.State)) #frequency distribution
print(df.Index.value_counts(ascending=True))

