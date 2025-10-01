'''
Aim :
Perform the following operation on the given dataset.
(Each batch data set is different )
a) Load the Data set
b) Find the Shape of Data
c) Find the summary of the data
d) Find the data type of each column
e) Find Missing Values
f) Finding out Zero's
g) Find Mean
h) Replace the missing values
i) Draw the pair plot
j) Create subsets as per the given instructions
k) divide the dataset into training (75%) and testing (25%).
'''
import pandas as pd 

df = pd.read_csv("sales_data_sample.csv",encoding="latin1")

# print(df.shape) 
# print(df.describe())
col = df.columns
print(col.dtype) #object


print(df.mean(numeric_only=True))

# df["POSTALCODE"].fillna(df["POSTALCODE"].mode()[0] , inplace=True)
# print(df["POSTALCODE"].isnull().sum())

# print(df["POSTALCODE"])

remove_all_null_values = df.fillna(df.mode().iloc[0] )
print(remove_all_null_values.isnull().sum().sum()) #0








