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
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split

df = pd.read_csv("sales_data_sample.csv",encoding="latin1")

print(df.shape) 

print(df.describe())
col = df.columns

print(col.dtype) #object

df.isnull().sum

zeros_count = (df==0).sum()   # () used for the condition purpose 
print(zeros_count)

print(df.mean(numeric_only=True))

# METHOD TO REMOVE ALL THE NULL\NAN VALUES FROM THE DATASET 
remove_all_null_values = df.fillna(df.mode().iloc[0] )   #.fillna("takes the value to filled with eg: df.mode()iloc[0]")    
print(remove_all_null_values.isnull().sum().sum()) #0
df = remove_all_null_values
print(df.isnull().sum()) #0

# fillna specific col wise 
# df["POSTALCODE"].fillna(df["POSTALCODE"].mode()[0] , inplace=True)
# print(df["POSTALCODE"].isnull().sum())


sns.pairplot(df)
plt.show()

#unwanted features ! data cleaning 
df = df.drop(columns=['ORDERNUMBER', 'ORDERDATE', 'PRODUCTCODE', 
    'CUSTOMERNAME', 'PHONE', 'ADDRESSLINE1', 'ADDRESSLINE2',
    'CONTACTLASTNAME', 'CONTACTFIRSTNAME'])

x=df.drop(columns= ['SALES'] , axis= 1) # all the df other than sales 
y= df['SALES'] # contain only sales data

 # Convert categorical to numeric
x_encoded = pd.get_dummies(x , drop_first=True)
# Split 
x_train , x_test , y_train , y_test = train_test_split(x_encoded , y , test_size=0.25 , random_state=42)
print(x_train)
print(x_test)
print(y_train)
print(y_test)










