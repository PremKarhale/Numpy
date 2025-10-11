# head
# tail
import pandas as pd
df =pd.read_csv("sales_data_sample.csv",encoding="latin1")
# print("Display 10 first rows of dataset ")
# print(df.head(10))
# print("Display 10 last rows of dataset ")
# print(df.tail(10))

print(df.info()) # tells us about the no of rows,coloumns or datatypes  


